#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_01_2018  20:30
  File Name:      /GitHub/sliding
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  主要解决极验验正码
  通过查看网页可以发现滑动验证码的图片由两张图片组成。
  需要注意的是在查看图片是可以发现每张图片是由52张小图片组合而成。
  而每一张小图片其实都是一样的，通过偏移拼接出了正常的图片。

  每张图片都有偏移
    鼠标放上验证码的时候，能看到div里面元素的变化，记住变化后的，修改成
    然后把鼠标移到下面的碎图片上就能看到每张图片对应的位置

==============================
"""
import time

__author__ = 'Loffew'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标滑动
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
import requests
import re
from io import BytesIO


def merge_image(image_file, position_list):
    im = Image.open(image_file)
    new_im = Image.new("RGB", (312, 116))  # 新建一个图（jpg图片保存后，属性里面能看到）
    # 一行26个312宽度，每个宽度12，高度58，两行，116
    #
    # 切割图片
    im_list_upper = []
    im_list_down = []
    for x, y in position_list:
        if y == -58:
            im_list_upper.append(im.crop((abs(x), 58, abs(x)+10, 116)))
        if y == 0:
            im_list_down.append(im.crop((abs(x), 0, abs(x)+10, 58)))

    up_offset = 0
    for im in im_list_upper:
        new_im.paste(im, (up_offset, 0))  # 把小图片放到新的空白图片上
        up_offset += im.size[0]  # im.size返回的是x，y的值

    do_offset = 0
    for im in im_list_down:
        new_im.paste(im, (do_offset, 58))  # 下面排的图片
        do_offset += im.size[0]
    new_im.show()
    return new_im


def get_image(driver, div_path):
    """
    获取div里面的图片
    两张图片的class
        gt_cut_bg gt_show       '//*[@id="captcha"]/div/div[1]/div[2]/div[1]/a[1]/div[1]'
                                或者 '//*[@class="gt_cut_bg gt_show"]'
        gt_cut_fullbg gt_show   '//*[@id="captcha"]/div/div[1]/div[2]/div[1]/a[2]/div[1]'
                                或者 '//*[@class="gt_cut_fullbg gt_show"]'

    """
    time.sleep(2)
    background_images = driver.find_elements_by_xpath(div_path)

    url_regx = re.compile(r'url\("(.*?)"\)')
    position_list = []
    for i in background_images:
        # 获取图片，偏移量
        img_url = i.get_property('style').get('background-image')
        url = url_regx.findall(img_url)[0]
        x = int(i.get_property('style').get('backgroundPositionX')[:-2])
        y = int(i.get_property('style').get('backgroundPositionY')[:-2])
        # print(x, y)
        position_list.append((x, y))
    # 保存图片
    image_file = BytesIO(requests.get(url).content)  # 此为无序图片，通过IO保存到内存
    image = merge_image(image_file, position_list)
    return image

def is_simpil(image1, image2, x, y):
    """
    对比rgb的值
    :param image1:
    :param image2:
    :param x:
    :param y:
    :return:
    """
    pixel1 = image1.getpixel((x, y))
    pixel2 = image2.getpixel((x, y))
    for i in range(3):
        if abs(pixel1[i] - pixel2[i]) >= 50:
            return False
    return True

def get_move_location(image1, image2):
    """
    计算缺口位置
    也可以使用二值化，计算色差边距或者色块边缘像素位置的x值
    这里使用的是对比两张图片色差像素，获得像素x的值
    :param image1:
    :param image2:
    :return:
    """
    for i in range(0, 260):
        for j in range(0, 116):
            if is_simpil(image1, image2, i, j):
                return i

def get_track(pull):
    """
    模拟手动拖动
    :param pull:
    :return:
    """
    track = []  # 轨迹列表，执行的时候，按照这个轨迹来进行
    # 当前位移
    current = 0
    # 什么时候减速
    mid = pull*4/5  # 4/5的地方开始减速
    # 计算间隔
    t = 0.2  # 每0.2秒做一下动作
    # 初速度
    v = 0
    while current < pull:
        if current < mid:
            a = 2  # 加速度
        else:
            a = -0.5
        # 初速度
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 0.5 * a * t * t
        current += move
        track.append(round(move))

    for i in range(5):
        track.append(-1)

    return track


def main(driver):
    driver.get("http://cnbaowen.net/api/geetest")
    element = WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, "gt_slider_knob")))
    # 下载图片
    image1 = get_image(driver, '//*[@class="gt_cut_bg gt_show"]/div')
    image2 = get_image(driver, '//*[@class="gt_cut_fullbg gt_show"]/div')

    # 计算缺口位置
    pull_offset = get_move_location(image1, image2)
    track_list = get_track(pull_offset)

    # 开始滑动，要把动作模拟像
    ActionChains(driver).click_and_hold(on_element=element).perform()
    time.sleep(1.3)
    for track in track_list:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
    # 模拟人会返回一点
    ActionChains(driver).move_by_offset(xoffset=-1, yoffset=0).perform()
    time.sleep(1)
    ActionChains(driver).release(on_element=element).perform()


if __name__ == '__main__':
    try:
        start = webdriver.Firefox()
        main(start)
    finally:
        start.close()
