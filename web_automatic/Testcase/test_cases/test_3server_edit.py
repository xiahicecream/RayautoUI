# coding=utf-8
import time
from Testcase.pagemanagement.Serverpage import Serverpage
from Testcase.models.myunit_userlogin import MyTest
import unittest
from data import ReadExcel
class Server_edit(MyTest):
    # 输入服务器地址与激活码
    def test1_server(self):
        m=Serverpage(self.driver)
        self.a=m.edition_btn()
        time.sleep(1)
        #输入服务器地址为域名
        self.b=m.host_edit(ReadExcel('admintest',12,6))
        time.sleep(1)
        #输入激活码
        self.c=m.license_edit(ReadExcel('admintest',13,6))
        self.d=m.edit_ok()
        time.sleep(2)
        self.e=m.confirm_btn()
        time.sleep(15)
        self.f=m.license_titles()
        #验证激活码是否激活成功
        self.assertEqual(self.f,ReadExcel('admintest',13,9))
        time.sleep(5)

    #服务器按钮
    def test2_server(self):
        m=Serverpage(self.driver)
        # 重启服务器
        self.a=m.restart_btn()
        time.sleep(15)
        # 判断正在运行图标元素是否存在
        self.rest=m.is_ElementExist(ReadExcel('admintest',14,9))
        # 关闭服务器
        self.c=m.shutdown_btn()
        time.sleep(15)
        # 判断未运行图标元素是否存在
        self.stop=m.is_ElementExist(ReadExcel('admintest',15,9))
        # 启动服务器
        self.d=m.start_btn()
        time.sleep(15)
        # 判断正在运行图标元素是否存在
        self.star=m.is_ElementExist(ReadExcel('admintest',16,9))

