#coding=utf-8
import os

#定义文件目录
result_dir='D:/web_automatic/Testcase/report'
#获取目录下所有文件
lists=os.listdir(result_dir)

#重新按时间对目录下的文件进行排序
# Lambda 函数又叫匿名函数，冒号（：）前面fn 表示入参，冒号后面 表示返回值。lambda 和普通的函数相比，省去了函数名称

# os.path.getmtime()获取最新时间
lists.sort(key=lambda fn: os.path.getatime(result_dir+"/"+fn))
print('最新的文件为：'+lists[-1])

