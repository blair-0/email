#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2018/7/31 9:54
# @Author   : YZH
# @Email    : you_zhihong@aliyun.com
# @File     : sendEmail.py
# @Software : PyCharm
"""
向指定邮件列表文件发送邮件
Usage: ./script mail_list.txt
"""
import smtplib, random, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

mail_lists_file = sys.argv[1]
with open(mail_lists_file) as f:
    mail_lists = f.read().splitlines()

fromaddr = 'support@uniex.one'
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
    if len(toaddrs) == 10:
        msg['To'] = ",".join(toaddrs)
        with smtplib.SMTP('smtp.dot618.com', 587) as server:
            server.starttls()
            server.login('yzh@dot618.com', 'slee@1092')
            server.sendmail(fromaddr, toaddrs, msg.as_string())
        toaddrs.clear()
        # 如果不删除则每次都会追加
        del msg['To']
        # 每次发送间隔时间为2-10分钟（163每天限制发送1000封左右）
        sleep(random.randrange(120, 600))
if toaddrs:
    msg['To'] = ",".join(toaddrs)
    with smtplib.SMTP('smtp.dot618.com', 587) as server:
        server.starttls()
        server.login('yzh@dot618.com', 'slee@1092')
        server.sendmail(fromaddr, toaddrs, msg.as_string())
