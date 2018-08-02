#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/7/31 9:54
# @Author   : YZH
# @Email    : you_zhihong@aliyun.com
# @File     : sendEmail.py
# @Software : PyCharm

import smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

fromaddr = 'support@uniex.one'
with open('/home/ec2-user/mail_lists/mail_163_20180730') as f:
    mail_lists = f.read().splitlines()
toaddrs = []
msg = MIMEMultipart('alternative')
msg['Subject'] = '邮件订阅回执'
msg['From'] = fromaddr

with open('/home/ec2-user/mail_msg/content.txt') as f1:
    msg_txt = f1.read()
with open('/home/ec2-user/mail_msg/content.html') as f2:
    msg_html = f2.read()

msg_part1 = MIMEText(msg_txt, 'plain')
msg_part2 = MIMEText(msg_html, 'html')

msg.attach(msg_part1)
msg.attach(msg_part2)

for addr in mail_lists:
    toaddrs.append(addr)
    if len(toaddrs) < 10:
        continue
    if  len(toaddrs) == 10:
        msg['To'] = ",".join(toaddrs)
        with smtplib.SMTP('smtp.dot618.com',587) as server:
            server.starttls()
            server.login('yzh@dot618.com', 'slee@1092')
            server.sendmail(fromaddr, toaddrs, msg.as_string())
        toaddrs.clear()
    sleep(random.randrange(60, 600))
if toaddrs:
    msg['To'] = ",".join(toaddrs)
    with smtplib.SMTP('smtp.dot618.com', 587) as server:
        server.starttls()
        server.login('yzh@dot618.com', 'slee@1092')
        server.sendmail(fromaddr, toaddrs, msg.as_string())
