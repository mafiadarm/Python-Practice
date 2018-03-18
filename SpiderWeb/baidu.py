#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           03_16_2018  20:35
  File Name:      /GitHub/baidu
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  不使用selenium 用封包登陆 http://www.baidu.com
  工具chaersi
==============================
"""
import io
import logging
import random

import math

import re
import requests
import time
import urllib3
from urllib.parse import urlencode

from PIL import Image

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)

"""
先跑通整个业务
    抓包之前先清理缓存
    要把所有可能碰到的情况都试一遍，如：账号错误，密码错误，验证码错误，最后才正确登陆
    抓完，清理干扰包
    保存

定位到关键的提交请求
    一般是post请求
    如果是登陆的话，是login等path，并能看到user，password等参数
    如果有验证码的话，可以看到正确的验证码
    不要每个包都去分析，太浪费时间，直接定位核心包
    百度登陆的核心请求：https://passport.baidu.com/v2/api/?login
登录页面
需要关注的参数：
token	73a60c0f542032b6d0ad3a8df9a8f93b
codestring	jxG2906c1f811cbe23b02df15154301f07e27b09807cc047b78
u	https://www.baidu.com/?tn=93882546_hao_pg
gid	52342BA-C1AC-4062-BBD0-8C67681E0D24
username	mumuloveshine
password	KQueIucNzF0fy78bKHTPQxYb0yrvcQ341y3zq0I86foUW9e+jGaTwwlgd2MSmMlWCPqJwZbXoim7wqbFuySCjDtz2gFWdrcDiL9I1b2rUWLN5b7vUHBItKXDGcS7g/UKzrm/aJcQn13f8eRJfUVw4RjczfLnnegXb0ZpdSmcnkE=
verifycode	女孩
rsakey	3zjTwwRNUqNpMMxX50CSKCc60K1EeLcx
ppui_logintime	20572
fp_uid	7585223da396030da1877f18e336f06f
fp_info	7585223da396030da1877f18e336f06f002~~~-z--XTorc-qimwX_q--buowm0m-95KO9GK_oowm0m-95KOmGK_V-lKrc-lKr~--rL-lyrOo0X-Lpzg9aWzCG8zmwJz9GLWC0nxLphwClmwC0tO9wtWm0oWSlFw90bjC0twm1lWSqLY9G8O90oOC0qxL-zgD~4TL-J_Gq-tJq-tSq-tCq-rxo0VlJpeYEp4NBpcoB-9QBHciEoDdL~QkEuh4B~4NBpcwc-qlDIDVB~cTPH9qB59qL-DdL5rTbIqNbH9UB-DXcoQmbIclPHZdE~qlDHeGB-WjDHWjsNk-DI6wPHeiCGoi9uFWsGoz9wtVBo0QADpc~bIcTEaWGB-QfEHWVb-4jPHeiLOFW908-9H8ODH4Nm09kDGKQmG8YbwJFb08OmGkkDG6GD1DNb-oz9H6GbGXW9Hnlm0q~9pbFmw8Qmwck9-4GbH8YSGohD~8QD~8WbGKW9-6km1oYC1KY90LOC1K-mGr~bG6Gb-DNm0mwD0DlbGlODp8Fm~4q9G4lmHbQ9G8-bGXzb0cx9pXwmHDqCpbjmwKjm~6qbH6N9Howb~JYm0o-b0tYmGmFbwmOD1LwD1twCp8Q9wcGm1tWC1lOCpXw9GJQb0J-CIWG90oWmwmFD0tQbw8jb~9N9pJF90lW9w9~b0oWDp8FC1rqbGX-DpXYbHmhD0oOmGK-mp8zmH4GmHb-m16kbGEkS~nqD~4QBanxb-efBIciPH9kEpqdB59x9G6qC0n~9GXwbwJO9wXwD1bWb0qlD09GbHmOD~bOb~XW90tjb-bFD~mOb-nq90DqmH9kD1rk90tYm06GC0EGbOWNCHDG91clD~8Wb0Xzm0bWDH9N9G4lbwoj91kqDGlFm1KODpcNmpX-C0bF9wXOmGqkbwqG9-XQ9GKO91XOmw6kHq-rRq-ryq-rwq-rZ--XMorR~Kf8jF_rowEHWUB~eOBK__-q-rI--tXq-tFq-tkq-taq-tPq-tWoVs0oi91Xh918FC1XwC1Lj9wXj98__
dv	tk0.276407821845840561518268251909@tto0zyAgPRnmX6D6Z06WtAL~wD6~hvnFhvLTCgBL57GJ~34kDfn1WRngnTvkI~4kqRCot7E~5hFCwv6tADLgopL~w~PyC-FStcB8pfA1DZ4kngATpTA-pp4tEhFWM8D6~vL~hF6teXntwvMLA3PWZVOJ6RAkI-n8pgngMe7k6RnmX6D6Z06WtAL~wD6~hvnFhvLTCgBL57GJ~34k6pAF2RngnTvmpp4tEhFWM8D6~vL~hF6teXntwvMLA3PWZVOJ6RA1qZnmpgngMeho0GyAkPT4k2yn-pZ7koR4kozA9pfAk2RngPX4koznkoRCot7E~5hFCwv6tADLgopL~wSOywfBL5CFsw9KJZmMszRngnTvk6pA8pXn1qRn1Wz78X6D6Z06WtAL~wD6~hvnFhvLThVPTATOT5W4kngATp~AkGRn1qz4kWT7FPRCot7E~5hFCwv6tADLgopL~wyBL5YB93kOyE38J~94kngATpgAkGRnF2p4koXng6f4mpgngMeyrrB~rIOwUvKhIoin8p-4kGf-ozMsRp412TA1DpAgI-nFIfAFIfnk6ynF6X7k2y7k2~nFWp7D__iobK0EfP0nb4-wTMTPUGStYB06UGywc4-X~OSE3BS3UBJD_Fopn12p4mfZn-pXnk6~4kng7mpXngGy4kPy7mpXngGy4kop7FDRAknXwo0vrnmpg78pyn-py7mpTn8pZ78pXnknRnFqZ4kogA8pXAk6RnFDz4ko~n8pX7kGRn1G-4k2znHp-7k6RngqX4kn-A8pgn1PRngnf4kngAp__
traceid	1B8DFC01

通过taoken这种参数，几乎都是服务器传过来的，直接搜索response
通过搜索得到https://passport.baidu.com/v2/api/?login，分析上面的页面得到关键字gid，再去查找gid
    类似于1521203972553 基本都是13位时间戳 或者还有10位的时间戳
    类似 [tpl mu] [apiver xx] 这种都是固定值，照写就行 
通过 ctrl + F 搜索gid的值，未找到，大概判断是客户端JS代码生成
接着搜索gid这个key，可以勾选whole words only，定位到js文件，如果有多个，得一个个去查找[这里没技巧]
https://ss0.bdstatic.com/5LMZfyabBhj3otebn9fn2djv/passApi/js/loginv4_f53550e.js
通过浏览器，清理缓存后，访问到特定登录前的位置，目的一就是加载所有的js资源，
访问上一步定位的js文件，格式化，搜索gid，可以定位到 gid = + t.guideRandom，再搜索 guideRandom 去找算法，得到gid算法函数
把这个函数算法转成python函数
"""


class BaiDu:
    """
    建立一个测试的python文件，并且编写一个类
        init方法中，实例化requests，的session
        按照访问顺序,建立入口方法和一次访问的方法
        一般写1到2个方法就测试一下
    visit_api 方法出现，未得到想要的文件
    requests进行代理设置，抓取程序访问的数据
        比对程序发送的https://passport.baidu.com/v2/api/ 请求和浏览器发送的数据的差异
            比对headers，写成一模一样
            比对params，多次抓取百度的数据，可以发现callback = 的value，每次都会变化，而且变化的结果最后那点变化
            在response body中搜索bd_cbs_ 或 callback (以外得到bd_pcbs_)
            最后得到算法 e.getUniqueID = function() 转成python
    大部分网站的callback是可以不用填写的，直接去掉这个参数不提交，而且得到的返回值会由 字典 直接变成 json字符串
    但是百度不可以，必须提交callback
    参数中dv过于太复杂，也因为可以不提交，所以不需要弄
    访问getpublickey没有任何难度

    在登陆login页面提交之前，需要获取验证码，并进行验证
        https://
        根据之前得到的codeString获取到验证码图片
        保存后校验验证码
    """
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.baidu.com',
        'Referer': 'https',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.132Safari/537.36',
    }

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

        self.s = requests.session()
        self.s.verify = False
        self.s.headers = self.header

        self.s.proxies = {"https": "127.0.0.1:8888"}  # 挂到抓包工具上获取数据进行比较

    def start(self):
        self.visit_index()
        time.sleep(0.5)
        self.visit_api()
        time.sleep(0.5)
        self.visit_checklogin()
        time.sleep(0.5)
        self.get_publickey()
        time.sleep(0.5)
        self.visit_checkvecode()
        time.sleep(0.5)


    def visit_index(self):
        url = "https://www.baidu.com"
        self.s.get(url)

    def visit_api(self):
        url = "https://passport.baidu.com/v2/api/?getapi&"
        self.gid = gid_encrypt()  # 前面gid获取靠转换js成python那个函数
        params = {
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_13_time(),
            'class': 'login',
            'gid': self.gid,
            'loginversion': 'v4',
            'logintype': 'dialogLogin',
            'traceid': '',
            'callback': self.get_call_back(),
        }
        url = url + urlencode(params)
        r = self.s.get(url)
        r.encoding = "UTF-8"

        self.token = get_first_str_by_text_multi('"token".*?:.*?(.*?)', r.text)  # 写个正则去获取token
        print('得到token')


    def visit_checklogin(self):
        url = "https://passport.baidu.com/v2/api/?logincheck&"
        params = {
            'token': self.token,
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_13_time(),
            'class': 'login',
            'loginversion': 'v4',
            'logintype': 'dialogLogin',
            'traceid': '',
            'callback': self.get_call_back(),
        }
        url = url + urlencode(params)
        r = self.s.get(url)
        r.encoding = 'utf-8'
        text = r.text
        self.codeString = get_first_str_by_text_multi('"codeString".*?:.*?"(.*?)"', text)
        self.vcodetype = get_first_str_by_text_multi('"vcodetype".*?:.*?"(.*?)"', text)
        print("得到codeString和vcodetype")

    def get_publickey(self):
        url = ""
        params = {
            'token': self.token,
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_13_time(),
            'gid': self.gid,
            'loginversion': 'v4',
            'traceid': '',
            'callback': self.get_callback(),
        }

        r = self.s.get(url, params=params)
        r.encoding = 'utf-8'
        text = r.text
        self.pubkey = get_first_str_by_text_multi('''"pubkey".*?:.*?'(.*?)',''', text)
        self.key = get_first_str_by_text_multi('''"key".*?:.*?'(.*?)',''', text)
        print("得到pubkey和key")

    def get_call_back(self, e=""):
        return e + to_string_private(math.floor(2147483648 * random.random()), 36)  # toString(36)需要自己实现一下36位转换[见课件]

    def visit_get_vcode(self):
        url = "https://passport.baidu.com.cgi/genimage?" + self.codeString
        r = self.s.get(url)
        f_img = io.BytesIO(r.content)
        im = Image.open(f_img)
        im.save("baidu_vcode.img")

    def visit_genimage(self):
        pass

    def visit_checkvecode(self):
        vcode = input('请输入验证码')
        url = 'https://passport.baidu.com/v2/?checkvcode&a=1&a=2&a=3&a=4&'
        params = {
            'token': self.token,
            'tpl': 'mn',
            'apiver': 'v3',
            'tt': get_13_time(),
            'verifycode': vcode,
            'loginversion': 'v4',
            'codestring': self.codeString,
            'traceid': '',
            'callback': self.get_callback(),
        }
        url = url + urlencode(params)
        r = self.s.get(url)
        r.encoding = 'utf-8'
        text = r.text

def gid_encrypt():
    s_raw = 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'

    s_ret = ''
    for s in s_raw:
        t = random.randint(0, 16)
        if 'x' == s:
            n = t
            s_ret += hex(n)[-1:]
        elif 'y' == s:
            n = 3 & t | 8
            s_ret += hex(n)[-1:]
        else:
            s_ret += s

    return s_ret.upper()

def get_first_str_by_text_multi(p, text):
    ll = re.findall(p, text, re.M | re.S)
    return ll[0]

def to_string_private_1(num, n):
    return ((num == 0) and "0") or (to_string_private_1(num // n, n).lstrip("0") + "0123465789abcdefhijklmnopqrstuvwxyz"[num % n])


def to_string_private(num, n):
    """
    上面的表达式也可以写成这个
    """
    n_chars = "0123465789abcdefhijklmnopqrstuvwxyz"
    if num == 0:
        return "0"
    else:
        x, y = divmod(num, n)  # divmod 返回一个商[整除]， 一个余数
        return to_string_private(x, n).lstrip("0") + n_chars[y]


def get_13_time():
    """
    获得13位时间戳
    :return:
    """
    return str(int(time.time()*1000))

if __name__ == '__main__':
    user = ""
    pwd = ""
    baidu = BaiDu(user, pwd)
    baidu.start()
