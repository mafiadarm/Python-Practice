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
    """

    text = str(pyperclip.paste())  # 粘贴板赋值
    infoList = text.splitlines()  # 分行变成list

    for info in infoList:
        info_strip = info.strip()

        # 去除带HTTP信息的头,  # 去除Cookie信息
        if info_strip.endswith('HTTP/1.1') or info_strip.startswith("Cookie"):
            infoList.remove(info)

    if "\t" in text:  # 处理分隔符
        tag = "\t"
    elif ":" in text:
        tag = ":"
    elif "=" in text:
        tag = "="

    result = []
    for i in infoList:
        key, value = i.split(tag, maxsplit=1)
        result.append(f"'{key.strip()}': '{value.strip()}',")

    headers = "\n".join(result)

    print(headers)
    pyperclip.copy(headers)  # 返回粘贴板


if __name__ == '__main__':
    disposeHead()


