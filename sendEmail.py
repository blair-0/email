#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/7/31 9:54
# @Author   : YZH
# @Email    : you_zhihong@aliyun.com
# @File     : sendEmail.py
# @Software : PyCharm

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = 'admin@uniex.one'
toaddrs = '379975166@qq.com'
msg = MIMEMultipart('alternative')
msg['Subject'] = '邮件订阅回执'
msg['From'] = fromaddr
msg['To'] = toaddrs

with open('/home/ec2-user/mail_msg/content.txt') as f1:
    msg_txt = f1.read()
with open('/home/ec2-user/mail_msg/content.html') as f2:
    msg_html = f2.read()

msg_part1 = MIMEText(msg_txt, 'plain')
msg_part2 = MIMEText(msg_html, 'html')

msg.attach(msg_part1)
msg.attach(msg_part2)

server = smtplib.SMTP('smtp.dot618.com',587)
server.starttls()
server.login('yzh@dot618.com', 'slee@1092')
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
