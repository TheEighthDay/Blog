#!/usr/bin/python
#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart


# 第三方 SMTP 服务
mail_host = "smtp.sina.cn"
mail_port = 465  # 也可能是25，看情况。SMTPS的话一般是465
mail_user = "13547880263@sina.cn"
mail_pass = "WEI131494250"   # 密码或邮箱授权码

mail_sender = '13547880263@sina.cn'
mail_receivers = ['13547880263@sina.cn']

message = MIMEMultipart()
subject = 'Blog message'
message['From'] = formataddr(["The Message from TheEighthDayPage", "13547880263@sina.cn"])
message['To'] = formataddr(["Me", "13547880263@sina.cn"])
message['Subject'] = Header(subject, 'utf-8')

#att1 = MIMEText(open('stmp.py', 'rb').read(), 'base64', 'utf-8')
#att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#att1["Content-Disposition"] = 'attachment; filename="stmp.py"'
#message.attach(att1)


def sendmail(host, port, sender, password, recvivers, meassage):
    try:
        mail_obj = smtplib.SMTP_SSL()  # 邮件服务器使用 SMTPS 的时候用 SMTP_SSL
        mail_obj.connect(host, port)
        mail_obj.login(sender, password)
        mail_obj.sendmail(sender, recvivers, meassage.as_string())
        mail_obj.quit()
        return True
    except Exception as e:
        err = "Send Failed for reason:\n {}".format(e)
        print(err)
        return False

def send(text):
    message.attach(MIMEText(text, 'plain', 'utf-8'))
    return sendmail(mail_host, mail_port, mail_sender, mail_pass, mail_receivers, message)
