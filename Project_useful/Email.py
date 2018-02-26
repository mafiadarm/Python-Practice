# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_23_2018  14:02
   File Name:      /GitHub/Email
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

__author__ = 'Loffew'

import logging
import smtplib
import imapclient
import pyzmail
import pprint

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

# 没法连接
# SMTP_ADDRESS = "smtp.gmail.com"
# PORT = 587
# smtpObj = smtplib.SMTP(SMTP_ADDRESS, PORT)
# type(smtpObj)
# smtpObj.starttls()

SMTP_ADDRESS = "smtp.rosun.com.cn"
PORT = 465
# smtpObj = smtplib.SMTP_SSL(SMTP_ADDRESS, PORT)  # 连接服务器
# pp_dbg(smtpObj.ehlo())  # 检查连接成功否

# 发送邮件
sendEmail = "zhongshuai@rosun.com.cn"
getEmail = "zhongshuai@rosun.com.cn"
emailText = "Subject: This is Object\nDear loffew,this is text, loffew"
# smtpObj.sendmail(sendEmail, getEmail, emailText)
# smtpObj.quit()

# 登陆到smtp服务器
IMAP_ADDRESS = "imap.qq.com"
mySelfEmail = "18888888@qq.com"  # 填入自己的qq邮箱
imapObj = imapclient.IMAPClient(IMAP_ADDRESS, ssl=True)
passWord = "获取到的"  # qq密码或从邮箱开启服务，获取验证码
imapObj.login(mySelfEmail, passWord)

# 文件夹
# pprint.pprint(imapObj.list_folders())

# 选择文件夹
imapObj.select_folder("INBOX", readonly=True)

# 搜索
UIDs = imapObj.search(["SINCE 2017-7-29"])  # 返回指定消息
# pprint.pprint(imapObj.fetch(106, ["BODY[]"]))

# 分析邮件内容
ss = imapObj.fetch(106, ["BODY[]"])[106][b'BODY[]']  # 返回的是嵌套字典所以又取出来
message = pyzmail.PyzMessage.factory(ss)
print(message.get_subject())
print(message.get_address("from"))
print(message.get_address("to"))

# 获取文本
print(message.html_part.get_payload().decode("utf-8"))

# 删除邮件
# imapObj.delete_messages(UIDs)
# imapObj.expunge()

# 断开
imapObj.logout()