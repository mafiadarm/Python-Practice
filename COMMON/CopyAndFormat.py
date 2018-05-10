# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_30_2018  12:58
   File Name:      /GitHub/json_format
   Creat From:     PyCharm
   Python version:
- - - - - - - - - - - - - - - 
   Description:    格式化从抓包软件复制的head信息，成为json格式
                   用法：复制后，执行，粘贴出来就是格式化后的内容
==============================
"""
import pyperclip
import logging

__author__ = 'Loffew'


def disposeHead():
    """
    Copy text for HEAD COOKIES
    like {
	CONNECT www.googleapis.com:443 HTTP/1.1
    Host	www.googleapis.com:443
    Proxy-Connection	keep-alive
    User-Agent	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    }
    :return:
    """
    global result
    text = str(pyperclip.paste())  # 粘贴板赋值
    infoList = text.splitlines()  # 分行变成list

    if 'HTTP/1.1' in infoList[0]:  # 去除带HTTP信息的头
        infoList.pop(0)
    if infoList[0].startswith('Host'):  # 去除Host信息
        infoList.pop(0)
    if infoList[-1].startswith('Cookie'):  # 去除Cookie信息
        infoList.pop(-1)

    if "\t" in text:  # 处理分隔符
        result = ["'%s': '%s'," % (i.split("\t")[0], i.split("\t")[1]) for i in infoList]
    elif ":" in text:
        result = ["'%s': '%s'," % (i.split(":")[0].replace(" ", ""), i.split(":")[1].replace(" ", "")) for i in
                  infoList]
    elif "=" in text:
        result = ["'%s': '%s'," % (i.split("=")[0], i.split("=")[1]) for i in infoList]

    pyperclip.copy("\n".join(result))  # 返回粘贴板


if __name__ == '__main__':
    disposeHead()
