#coding=utf-8
from Testcase.pagemanagement.LoginPage import LoginPage
from Testcase.pagemanagement.Admin_edit import Admin_edit
from data import ReadExcel
from Testcase.models.myunit_userlogin import MyTest
from Testcase.models.myunit import Mytestnew
from selenium import webdriver
import time
import unittest
class Ademin_edit(MyTest):

    # 修改管理员密码
    def test1_admin(self):
        m=Admin_edit(self.driver)
        self.a=m.admin_click()
        self.b=m.admin_edit()
        time.sleep(1)
        self.c=m.admin_account(ReadExcel('admintest',35,6))
        self.d=m.admin_old(ReadExcel('admintest',36,6))
        self.e = m.admin_new(ReadExcel('admintest', 37, 6))
        self.f= m.admin_newcom(ReadExcel('admintest', 38, 6))
        self.g=m.adminok_btn()
        time.sleep(2)
