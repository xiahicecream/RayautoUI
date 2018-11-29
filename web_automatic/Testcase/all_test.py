# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unittest
import HTMLTestRunner
import time,os
from email.header import Header

# 发送邮件
def send_mail(file_new):
    sender = 'iicecream@qq.com'
    # 接受邮箱
    receiver = ['iicecream@qq.com']

    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    username = 'iicecream@qq.com'
    password = 'kfkqxveyatcvbhff'


    msgRoot=MIMEMultipart()
    # 添加正文,遍历报告内的文字
    msgRoot['From']=Header(u"雪糕",'utf-8')
    # 主题
    subject='镭速管理员后台自动化测试报告'
    msgRoot['subject']=Header(subject,'utf-8')
    # 打开最新文件
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()
    # 添加正文
    msgRoot.attach(MIMEText(mail_body,_subtype='html',_charset='utf-8'))

    # 添加附件
    att = MIMEText(open(file_new, 'rb').read(), 'base64','uft-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="result report.html"'
    msgRoot.attach(att)

    # 定义发送时间
    msgRoot['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    try:
        smtp=smtplib.SMTP_SSL(smtpserver,465)
        smtp.login(username,password) #发送的账号密码
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()
        print('邮件已发送')
    except smtplib.SMTPException:
        print ('邮件发送不成功')






# 查找测试报告目录，找到最新生成的测试报告文件

def send_report(testreport):
    # 定义文件目录
    result_dir = testreport
    # 获取目录下所有文件
    lists = os.listdir(result_dir)

    # 重新按时间对目录下的文件进行排序
    # Lambda 函数又叫匿名函数，冒号（：）前面fn 表示入参，冒号后面 表示返回值。lambda 和普通的函数相比，省去了函数名称

    # os.path.getmtime()获取最新时间
    lists.sort(key=lambda fn: os.path.getatime(result_dir + "/" + fn))
    print('最新的文件为：' + lists[-1])

    # 找到最新生成的文件
    file_new=os.path.join(result_dir,lists[-1])
    print(file_new)
    # 调用发邮件模块
    send_mail(file_new)



def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='D:/web_automatic/Testcase/test_cases'
    #定义discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py',top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        print(test_case)
        testunit.addTests(test_case)
    return testunit
if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    testreport="D:/web_automatic/Testcase/report/"
    filename = testreport+now+"result.html"
    fp = open(filename, mode='wb')  # WB已读写方式打开文件
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,  # 制定测试报告文件
        title=u'后台管理员登录测试报告',  # 报告标题
        description=u'用例执行情况：',) # 报告副标题
    alltestnames = creatsuite()
    runner.run(alltestnames)
    # 关闭生成的报告
    fp.close()
    send_report(testreport)









# coding=utf-8
# import unittest
# import time
# import HTMLTestRunner
# from Testcase.test_cases import admin_add,login_sta
# suit=unittest.TestSuite()
# suit.addTest(login_sta.AdminLoginTest('test1_login'))
# suit.addTest(login_sta.AdminLoginTest('test2_login'))
# suit.addTest(login_sta.AdminLoginTest('test3_login'))
# suit.addTest(login_sta.AdminLoginTest('test4_login'))
# suit.addTest(login_sta.AdminLoginTest('test5_login'))
# suit.addTest(admin_add.AdminaddTest('test1_adminadd'))
# if __name__ == '__main__':
#     #获取当前时间
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     filename = "D:/web_automatic/Testcase/report/"+now+"result.html"
#     fp = file(filename, 'wb')  # WB已读写方式打开文件
#     # 定义测试报告
#     runner = HTMLTestRunner.HTMLTestRunner(
#         stream=fp,  # 制定测试报告文件
#         title=u'后台管理员登录测试报告',  # 报告标题
#         description=u'用例执行情况：',  # 报告副标题
#     )
#     # 运行测试用例
#     runner.run(suit)
#     # 关闭报告文件
#     fp.close()
