#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           06_28_2018  11:03
    File Name:      /GitHub/sangfor_report
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""
import requests

__author__ = 'Loffew'

base_url = "http://10.0.10.15:8888"
url = "/src/acloglogin.php"

s = requests.session()

head = {
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': '10.0.10.15:8888',
    'DNT': '1',
}

data = {
    'login_user': 'admin',
    'login_password': 'rosun*95321432',
    'login': 'true',
}

rr = s.get(url=base_url+"/src/acloglogin.php", headers=head)
print(rr.text.encode("utf-8").decode("gbk"))
# ee = s.post(url=base_url+url, data=data)
# print(ee.status_code)