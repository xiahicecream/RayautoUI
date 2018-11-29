#coding=utf-8
import os,time
k=1
while k<2:
    now_time=time.strftime('%H_%M')
    if now_time=='18_25':   #下午6点运行脚本
        print (u'开始运行脚本：')
        os.chdir("D:/web_automatic/Testcase")#查找脚本所在路径
        os.system('python all_test.py') #执行脚本
        print (u'运行完成退出')
        break
    else:
        time.sleep(10)
        print (now_time)