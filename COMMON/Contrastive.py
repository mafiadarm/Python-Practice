#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           06_10_2018  21:24
  File Name:      /GitHub/Contrastive
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
__author__ = 'Loffew'


def contrast(con_1, con_2):
    for key, value in con_1.items():

        if value == con_2[key]:
            pass
        else:
            print(key, "\t\t", value)
            print(key, "\t\t", con_2[key])

if __name__ == '__main__':
    contrast_1 = {  # Format content from CopyAndFormat.py
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'qrcode_flag': 'false',
        'useticket': '1',
        'pagerefer': '',
        'vsnf': '1',
        'su': 'Tl9XT1JMREJCUw==',
        'service': 'miniblog',
        'servertime': '1528635666',
        'nonce': '0RMNDQ',
        'pwencode': 'rsa2',
        'rsakv': '1330428213',
        'sp': '5139784953d40d11cb250cfefce9145a5106f2e44ad1f95057b27b9d0c2aad9797f89da3f771c0ff27fa524b8f957cb7d2479adc2b2b7e19c4af70357929140641af1bce8f1d494753b3a8742a4a672b2b195cde74fc691f4be12709171bcab7a2eb2af387154664fac1ab7d2fb390c7270dd7bbcc276dc8f989f5fb0cc9e83c',
        'sr': '1920*1080',
        'encoding': 'UTF-8',
        'prelt': '37',
        'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META',
    }

    contrast_2 = {  # Format content from CopyAndFormat.py
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'qrcode_flag': 'false',
        'useticket': '1',
        'pagerefer': '',
        'vsnf': '1',
        'su': 'bl93b3JsZGJicw==',
        'service': 'miniblog',
        'servertime': '1528637456',
        'nonce': '2FBLJ1',
        'pwencode': 'rsa2',
        'rsakv': '1330428213',
        'sp': 'c844294a1d7fa3d1f8176d18f2fe01a786d475b5daf05db9da72942708f327a46b6434d0adb6153f000b56ec0385d2f35ecd3e076f5235b817f9465c31fbf7bde49d03a58e09f0c1ef0e489cf778477910a137a4303c44d1ad3d3fe0bfe6fbb9dcce91720ad3c42d9ab87b4c645fdf463329734444445f593fbdef7c65bffd4d',
        'sr': '1920*1080',
        'encoding': 'UTF-8',
        'prelt': '45',
        'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META',
    }

    contrast(contrast_1, contrast_2)

