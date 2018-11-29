# coding=utf-8
import time
from data import ReadExcel,writeExcel


from Testcase.models.myunit import MyTest
from Testcase.pagemanagement.LoginPage import LoginPage


class AdminLoginTest(MyTest):
    # 输入含有非法字符的账号
    def test1_login(self):
        m = LoginPage(self.driver)
        self.u=m.set_username(ReadExcel('admintest',6,6))
        self.p=m.set_password(str(ReadExcel('admintest',6,7)))
        self.c=m.click()
        time.sleep(2)
        self.e=m.get_errortitle()
        self.assertEqual(self.e,ReadExcel('admintest',6,9))
        # writeExcel(0 , 6, 10, self.e)




    # # 输入正确的账号错误的密码
    def test2_login(self):
        m = LoginPage(self.driver)
        self.u = m.set_username(ReadExcel('admintest',7,6))
        self.p = m.set_password(str(ReadExcel('admintest',7,7)))
        self.c = m.click()
        time.sleep(2)
        self.e = m.get_errortitle()
        self.assertEqual(self.e, ReadExcel('admintest',7,9))
        # writeExcel(0, 7, 10, self.e)




    # # 输入空的账号,正确的密码
    def test3_login(self):
        m = LoginPage(self.driver)
        # self.u=m.set_username(' ')
        self.p = m.set_password(str(ReadExcel('admintest',8,7)))
        time.sleep(2)
        self.c = m.click()
        time.sleep(2)
        self.e = m.get_errortitle()
        self.assertEqual(self.e,ReadExcel('admintest',8,9))
        # writeExcel(0, 8, 10, self.e)


    # # 输入正确的账号，空的密码
    def test4_login(self):
        m = LoginPage(self.driver)

        self.u = m.set_username(ReadExcel('admintest',9,6))
        # self.u=m.set_password(' ')
        time.sleep(2)
        self.c = m.click()
        time.sleep(2)
        self.e = m.get_errortitle()
        self.assertEqual(self.e,ReadExcel('admintest',9,9))
        # writeExcel(0, 9, 10, self.e)



    # # # 输入正确的账号密码
    def test5_login(self):
        m = LoginPage(self.driver)
        self.u = m.set_username(ReadExcel('admintest',10,6))
        self.p =m.set_password(ReadExcel('admintest',10,7))
        self.c = m.click()
        time.sleep(4)
        self.f=m.get_DiaglogTitle()
        self.assertEqual(self.f, ReadExcel('admintest',10,9))
        time.sleep(1)
        # writeExcel(0, 10, 10, self.f)








