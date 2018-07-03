#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           06_13_2018  21:15
  File Name:      /GitHub/weibo_login
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  通过fiddler抓包，观察新浪微博登陆流程，模拟这个登陆流程进行爬虫
  密码加密是根据网页js跟踪发现是rsa加密，公钥在明文中传递，私钥在js中
  登陆方式为post后，返回一个网址，get，再返回，再get，得到最终显示的内容
  实现其功能的js函数为location.replace
==============================
"""
import json
import logging
import time

import re

import binascii
import requests
import base64

import rsa

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


class Weibo_login:

    def __init__(self, username, password):
        self.user_name = username
        self.pass_word = password
        self.session = requests.session()
        self.session.headers.update({"UA": ""})  # 可以加一个头信息

    def get_password(self, servertime, nonce, pubkey):
        # 密码加密
        s = str(servertime) + "\t" + str(nonce) + "\n" + str(self.pass_word)
        public_key = rsa.PublicKey(int(pubkey, 16), int("10001", 16))
        password = rsa.encrypt(s.encode(), public_key)
        return binascii.b2a_hex(password).decode()

    def get_username(self):
        self.username = base64.b64encode(self.user_name.encode())

    def get_json_data(self):
        """
        从以下内容找到一些信息
        /sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=bl93b3JsZGJicyU0MHNpbmEuY29t&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_=1528896542846
        """
        params = {
            'entry': 'weibo',
            'callback': 'sinaSSOController.preloginCallBack',
            # base64的用户名，经测试为base64.b64encode(urllib.parse.quote(code).encode())
            # 如果用邮箱登陆就要用上面这个，如果是手机登陆就直接用
            'su': self.username,
            'rsakt': 'mod',
            'checkpin': '1',
            'client': 'ssologin.js(v1.4.19)',
            '_': int(time.time() * 1000),  # 13位时间戳
        }

        url = "https://login.sina.com.cn/sso/prelogin.php?"
        response = self.session.get(url=url, params=params)

        regx = re.compile(r"preloginCallBack\((.*?)\)")
        try:
            data_content = regx.findall(response.text)[0]
            json_data = json.loads(data_content)
        except:
            json_data = {}

        return json_data  # 如果出现验证码，在这里会出现一个参数showpin==1(验证码)

    def login(self):
        json_data = self.get_json_data()
        if not json_data:
            return False
        pass_word = self.get_password(json_data["servertime"], json_data["nonce"], json_data["pubkey"])

        post_data = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'qrcode_flag': 'false',
            'useticket': '1',
            # 'pagerefer': 'https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2F&domain=.weibo.com&ua=php-sso_sdk_client-0.6.28&_rand=1528896528.1563',
            'vsnf': '1',
            'su': self.username,
            'service': 'miniblog',
            'servertime': json_data["servertime"],
            'nonce': json_data["nonce"],
            'pwencode': 'rsa2',
            'rsakv': json_data["rsakv"],
            'sp': pass_word,
            'sr': '1920*1080',
            'encoding': 'UTF-8',
            'prelt': '196',
            'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META',
        }

        login_url = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)"

        # 登陆流程为post以后，返回一个地址，再请求这个地址，并且带上一些参数，才能获取结果

        # 第一次post请求
        response_data = self.session.post(url=login_url, data=post_data, verify=False)
        # print(response_data.content.decode("gbk"))

        # 获取返回的url
        # location.replace JS方法用于重新请求，不能点返回键返回，用于session安全
        reg_url = re.compile(r'location.replace\("(.*?)"\)')
        url = reg_url.findall(response_data.content.decode("gbk"))[0]
        # 再次请求
        url_again = self.session.get(url=url)
        # 获取最终url
        reg_url = re.compile(r"location.replace\('(.*?)'\)")
        final_url = reg_url.findall(url_again.content.decode("gbk"))[0]

        self.session.get(url=final_url, verify=False)

        print(self.session.get(url="https://weibo.com/u/2696956790/home", verify=False).content.decode())


if __name__ == '__main__':
    login = Weibo_login("username", "password")
    login.get_username()
    login.login()
