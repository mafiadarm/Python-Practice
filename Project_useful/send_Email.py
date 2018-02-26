# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_07_2018  13:25
   File Name:      /GitHub/send_mail
   Creat From:     PyCharm
   Python version: 3.6.2
- - - - - - - - - - - - - - - 
   Description:
   发送内容，需要用utf-8打开，不然有乱码，兼容GB2312
==============================
"""

import logging
import smtplib

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

def pp_dbg(*args):
    return logging.debug(*args)


smtp_server = "smtp.rosun.com.cn"  # smtp服务器地址
from_mail = "hq-it@rosun.com.cn"  # 邮件账号
mail_pwd = "r0sun*953@143@"  # 登陆密码
to_mail = ["32336434@qq.com", "zhongshuai@rosun.com.cn"]  # 接收邮件的地址
cc_mail = ["gaowh@rosun.com.cn"]  # 抄送
from_name = "集团流程IT部"  # 发送者名称[可任意修改]
subject = "标题"  # 标题[可任意修改]
body = "测试内容"  # 内容[可任意修改]

mail = [
    "From: %s <%s>" % (from_name, from_mail),
    "To: %s" % ','.join(to_mail),
    "Subject: %s" % subject,
    "Cc: %s" % ','.join(cc_mail),
    "",
    body
]

msg = '\n'.join(mail)
msg = msg.encode("utf-8")  # 在客户端读取邮件的时候，如果出现乱码，要选择utf-8的编码

s = smtplib.SMTP(smtp_server)
s.login(from_mail, mail_pwd)
s.sendmail(from_mail, to_mail + cc_mail, msg)
s.quit()