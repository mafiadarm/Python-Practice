# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_07_2018  14:08
   File Name:      /GitHub/send_mail_html
   Creat From:     PyCharm
   Python version: 3.6.2
- - - - - - - - - - - - - - - 
   Description:
   把内容编辑成html来发送，打开邮件后，直接展示
==============================
"""

import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

def pp_dbg(*args):
    return logging.debug(*args)

def formatAddr(mail):
    name, addr = parseaddr(mail)
    return formataddr((Header(name, 'utf-8').encode(), addr))

smtp_server = "smtp.rosun.com.cn"  # smtp服务器地址
from_mail = "hq-it@rosun.com.cn"  # 邮件账号
mail_pwd = "r0sun*953@143@"  # 登陆密码

to_mail = ["32336434@qq.com", "zhongshuai@rosun.com.cn"]  # 接收邮件的地址
cc_mail = ["gaowh@rosun.com.cn"]  # 抄送

from_name = "集团流程IT部"  # 发送者名称[可任意修改]
subject = "标题"  # 标题[可任意修改]
body = "<h1>测试邮件</h1><h2 style='color:red'>This is a test</h1> "  # 内容[用网页方式发送]

msg = MIMEMultipart()  # 构造一个msg
msg["From"] = formatAddr("{} <{}>".format(from_name, from_mail))
msg["To"] = ','.join(to_mail)
msg["Subject"] = "标题"
msg.attach(MIMEText(body, 'html', 'utf-8'))

s = smtplib.SMTP(smtp_server)
s.login(from_mail, mail_pwd)
s.sendmail(from_mail, to_mail + cc_mail, msg.as_string())
s.quit()