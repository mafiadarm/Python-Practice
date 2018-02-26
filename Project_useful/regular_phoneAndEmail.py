# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_15_2018  19:48
   File Name:      /GitHub/project_regular_phone_number_e_mail
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:    查找电话和email的正则，使用方法：复制要查找的文本，运行py文件，粘贴出来就是结果
==============================
"""
__author__ = 'Loffew'

import pyperclip, re
# 创建电话正则
phoneRegex = re.compile(r"""(
(\d{3}|\(\d{3}\))?                # 区位号
(\s|-|\.)?                        # 分隔符
(\d{3})                            # 前三个数字
(\s|-|\.)                         # 分隔符
(\d{4})                            # 后四个数字
(\s*(ext|x|ext\.)\s*(\d{2, 5}))? # 扩展|分机
)""", re.VERBOSE)
# 创建email正则
emailRegex = re.compile(r"""(
[a-zA-Z0-9._%+-]+                  # 用户名
@                                   # @
[a-zA-Z0-9.-]+                     # 动态域名
(\.[a-zA-Z]{2,4})                  # 顶级域名
)""", re.VERBOSE)
# 匹配文本
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += " x" + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# 返回结果到粘贴板
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied tp clipboard:")
    print("\n".join(matches))
else:
    print("no phone no email")

