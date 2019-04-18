#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           01_09_2019  22:11
  File Name:      /Python-Practice/用云解析下载萌鸡小队
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import time
import requests
import re
from urllib.parse import unquote
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

__author__ = 'Loffew'


def error_log(file_name, source_url):  # 如果有报错存到文件里面
    with open("error.log", "a", encoding="utf-8") as ww:
        content = file_name + " " + source_url + "\n"
        ww.write(content)

def find_really_head(source_url=None):  # 用selenium去获取切割包的url
    cloud_url = "http://jiexi.92fz.cn/player/vip.php?url="  # 云解析接口一般为这种
    if not source_url: return False, False

    # 从selenium获取关键的url
    opt = webdriver.ChromeOptions()  # 创建chrome参数对象
    # opt.add_argument("--headless")  # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数，这里不适用（未知原因）
    prefs = {  # 设置flash自动开启，不然要手动去点，很悲剧
        "profile.managed_default_content_settings.images": 1,
        "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    }
    opt.add_experimental_option('prefs', prefs)
    get_url_from_frame = webdriver.Chrome(options=opt)  # 创建chrome无界面对象

    try:
        get_url_from_frame.get(cloud_url + source_url)

        get_url_from_frame.switch_to.frame(0)  # 第一层frame
        get_url_from_frame.switch_to.frame(0)  # 第二层frame
        guess_url = get_url_from_frame.find_element_by_xpath(r'//*[@id="tongdao"]/a')
        get_href = guess_url.get_attribute('href')
        really_url_head = re.findall(r"(http://.*?pass=)\d+.*?", get_href)[0]

        return get_url_from_frame, really_url_head
    except:
        print(cloud_url + source_url, "IS ERROR")
        return False, False

def use_selenium_get_cut_url(get_url_from_frame=None, really_url_head=None, road=None, source_url=None, return_url=None):
    if source_url:  # 如果有source_url就执行selenium
        get_url_from_frame, really_url_head = find_really_head(source_url)  # 获取链接头并回传diver
    if not get_url_from_frame: return False  # 如果之前报错，则此步骤直接停止

    road = 1 if not road else road  # 线路默认从1线开始
    source_url = return_url if not source_url else source_url  # 如果是递归则取用return的url值，如果是第一次，会有source传入，则不变
    really_url = really_url_head + str(road) + "&url=" + source_url  # 拼接url

    try:
        get_url_from_frame.get(really_url)
        for _ in range(road):
            get_url_from_frame.switch_to.frame(0)  # 有几线就进几层

        wait_flag = (By.ID, "ckplayer_a1")  # 设置等待，不然取不到元素
        WebDriverWait(get_url_from_frame, 20, 0.5).until(expected_conditions.presence_of_all_elements_located(wait_flag))

        guess_url = get_url_from_frame.find_element_by_xpath(r'//*[@id="ckplayer_a1"]/param[@name="flashvars"]')
        get_url = guess_url.get_attribute('value')  # 要去元素的值，不能直接用@，必须重新用get_attribute来取值

        get_url_from_frame.quit()
        return get_url
    except:
        if road < 5:
            print(really_url_head + source_url, "IS ERROR AND TRY AGAIN")
            use_selenium_get_cut_url(get_url_from_frame=get_url_from_frame, really_url_head=really_url_head, road=road+1, return_url=source_url)
        else:
            get_url_from_frame.quit()
            return False

def unquote_url(url):  # 转换一下url编码，正则好用
    return unquote(url)

def re_url(url):
    """
        用正则找出数据切割信息url和用于组合的url头部
        请求数据切割url返回切割包信息
        url头部在最后和切割好的内容拼接，去获取数据流
    """
    rule_url = re.compile(r"(http://.*?scid=\d+)")
    rule_head = re.compile(r"(http://.*?_mp4/)")
    try:
        url_find = rule_url.findall(url)[0]
        url_head = rule_head.findall(url)[0]
        return url_find, url_head
    except:
        print("WRONGING", url)

def get_lasts_url(url):  # 返回切割信息，因为是bytes字符，所以要用decode一下
    response = requests.get(url)
    return response.content.decode()

def text_to_list(content):  # 切割信息是一段str，让其成为列表
    text = content.split("\n")
    url_list = [i for i in text if "#" not in i][:-1]  # 去掉最后一个是空字符串的
    return url_list

def save_file(url_head, url_last_list, file_name):
    with open(file_name, "wb") as ww:
        for url_last in url_last_list:
            request_url = url_head + url_last
            response = requests.get(request_url, stream=True, timeout=10)  # 用数据流来获取信息
            if not response: error_log(file_name, request_url)
            for block in response.iter_content(1024):  # 分段写入
                if not block:
                    break
                ww.write(block)

def lazy_get_url_name():  # 这里偷了个大懒，直接复制了元素，然后用正则去取了
    url_head = "https://www.mgtv.com"
    with open("萌鸡小队", "r", encoding="utf-8") as rr:
        txt = rr.readlines()

    rule = re.compile(r'.*?title="(.*?)".*?href="(.*?)".*?')
    for i in txt:
        if not i: continue
        yield "D:/迅雷下载/萌鸡小队/" + rule.findall(i)[0][0] + ".mp4", url_head + rule.findall(i)[0][1]

def main(file_name, source_url):
        print("获得文件名和链接", file_name, source_url)
        find_url_in_frame = use_selenium_get_cut_url(source_url=source_url)
        if not find_url_in_frame:
            error_log(file_name, source_url)
            return "CAN NOT DOWNLOAD", file_name, source_url
        get_url = unquote_url(find_url_in_frame)
        cut, head = re_url(get_url)
        lasts_url_text = get_lasts_url(cut)
        lasts_url_list = text_to_list(lasts_url_text)
        save_file(head, lasts_url_list, file_name)

if __name__ == '__main__':
    # for name, _url in lazy_get_url_name():
    #     main(name, _url)
    main("王者之旅", "https://www.iqiyi.com/v_19rrnt8u2k.html?vfm=m_294_wgtv")