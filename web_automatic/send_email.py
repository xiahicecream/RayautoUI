# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time

# 发送邮箱
sender='iicecream@qq.com'
# 接受邮箱
receiver=['iicecream@qq.com']

# 发送邮箱服务器
smtpserver='smtp.qq.com'
username='iicecream@qq.com'
password='kfkqxveyatcvbhff'

msgRoot=MIMEMultipart('related')

# 发送邮件主题
msgRoot['subject']='Python email test'
# 构造附件
att=MIMEText(open('D:/web_automatic/Testcase/report/2017-11-27 17_23_50result.html','rb').read(),'base64','uft-8')
att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]='attachment; filename="2017-11-27 17_23_50result.html"'
msgRoot.attach(att)





try:
    smtpobj=smtplib.SMTP_SSL(smtpserver,465) #发送的邮箱服务器地址，端口
    smtpobj.login(username, password) #发送的账号密码
    smtpobj.sendmail(sender, receiver, msgRoot.as_string())
    print ('邮件发送成功')
except smtplib.SMTPException:
    print ('邮件发送不成功')