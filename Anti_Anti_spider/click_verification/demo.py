#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_08_2018  11:27
  File Name:      /GitHub/demo
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
import requests
from hashlib import md5
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


USERNAME = "908686161"
PASSWORD = "admin123"
SOFT_ID = 894600
KIND = 9004


class CrackTouClick:
    def __init__(self, username, password, soft_id):
        self.username = username
        self.password = md5(password.encode("utf8")).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            "user": self.username,
            "pass2": self.password,
            "softid": self.soft_id,
        }
        self.header = {
            "Connection": "Keep-Alive",
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
        }

    def post_pic(self, im, codetype):
        params = {
            "codetype": codetype,
        }
        params.update(self.base_params)
        files = {"userfile": ("ccc.jpg", im)}
        r = requests.post("http://upload.chajiying.net/Upload/Processing.php", data=params, files=files,
                          headers=self.header)
        return r.json()

    def report_error(self, im_id):
        params = {
            "id": im_id,
        }
        params.update(self.base_params)
        r = requests.post("http://upload.chajiying.net/Upload/ReportError.php", data=params, headers=self.header)
        return r.json()


class CrackTouClick_class:
    def __init__(self):
        self.url = "http://dun.163.com/trial/picture-click"
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.chaojiying = CrackTouClick(USERNAME, PASSWORD, SOFT_ID)

    def __del__(self):  # 实例结束的时候自动执行
        self.driver.close()

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=100"  # 往下拉一点点
        self.driver.execute_script(js)
        time.sleep(2)

    def get_touclick_element(self):
        element = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                       '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/img[1]')))
        return element

    def get_touclick_image(self, name='captcha.png'):
        time.sleep(2)
        self.driver.save_screenshot('aa.png')  # 当前屏幕截图
        element = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div')
        left = element.location['x']
        top = element.location['y'] - 100
        right = element.location["x"] + element.size['width']
        bottom = element.location['y'] + element.size['height']
        im = Image.open('aa.png')
        capthcha = im.crop((left, top, right, bottom))
        capthcha.save(name)
        return capthcha

    def points(self, result):
        groups = result.get("pic_str").split('|')
        locations = [[int(number) for number in group.split(",")] for group in groups]
        return locations

    def touch_click_words(self, locations):
        """
        对验证码进行点击
        :param locations: 点击位置
        :return:
        """
        # move_to_element_with_offset
        for location in locations:
            ActionChains(self.driver).move_to_element_with_offset(self.get_touclick_element(), location[0],
                                                                  location[1]).click().perform()
            time.sleep(2)

    def main(self):
        """
        主要执行逻辑，截图，上传，进行点击
        :return:
        """
        image = self.get_touclick_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format("PNG"))
        # 图
        result = self.chaojiying.post_pic(bytes_array.getvalue(), KIND)
        # print(result)
        locations = self.points(result)
        print(locations)
        # 解析坐标的方法
        self.touch_click_words(locations)
        time.sleep(3)
        # 判断是否验证成功
        try:
            success = self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[3]/div/div/div[2]/div[3]/span[2]'), '验证成功'))
        except:
            print("验证失败，重新上传")
        else:
            self.driver.save_screenshot("True.png")
            print(success)


if __name__ == '__main__':
    crack = CrackTouClick_class()
    crack.open()
    # crack.get_touclick_image()
    crack.main()
