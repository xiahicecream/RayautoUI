# coding=utf-8
import time


from Testcase.models.myunit_userlogin import MyTest
from Testcase.pagemanagement.User_addpage import Userddpage
from Testcase.models.random_number import random_user_name
import unittest
# import HTMLTestRunner



class UseraddTest(MyTest):
    # 创建正确的用户
    def test1_adminadd(self):
        #点击账户信息
        self.driver.find_element_by_css_selector('#user_info > span > span').click()
        time.sleep(2)
        #点击添加按钮
        self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > users > div:nth-child(2) > button').click()
        time.sleep(2)
        m = Userddpage(self.driver)
        self.u=m.set_username('xiaice1')
        self.a=m.set_account(random_user_name())
        self.p=m.set_password('Ruiyun123')
        self.ca=m.set_catalogue('/')
        self.r=m.set_rights()
        time.sleep(1)
        self.up=m.set_uploads('100')
        self.do=m.set_downloads('100')
        # self.em=m.set_email('382336995@qq.com')
        # self.n=m.set_phonenumber('13827362322')
        # self.c=m.set_companyName(u'云语')
        # self.z=m.set_address(u'科创大厦')
        self.f=m.set_remark('defefefdfef')
        self.h=m.set_click()
        time.sleep(2)
        self.e=m.get_normaltitle()
        self.assertEqual(self.e,u'用户列表')
    #删除用户
        time.sleep(2)
        self.deluser=m.del_user()
        time.sleep(1)
        self.con=m.del_confirm()
        time.sleep(5)









