#conding=utf-8
import time
from Testcase.pagemanagement.Configure import Configure_email,Configure_https,Configure_speed
from Testcase.models.read_fiels import read_files
from Testcase.models.myunit_userlogin import MyTest
from data import ReadExcel
import unittest
class Configur_edit(MyTest):
    #设置邮箱
    def test1_emailedit(self):
        m=Configure_email(self.driver)
        self.a=m.set_email()
        time.sleep(1)
        self.b=m.set_nickname(ReadExcel('admintest',18,6))
        self.c=m.set_fromemail(ReadExcel('admintest',19,6))
        self.d=m.set_smtphost(ReadExcel('admintest',20,6))
        self.e=m.set_smtpport(int(ReadExcel('admintest',21,6)))
        self.f=m.set_smtpaccount(ReadExcel('admintest',22,6))
        self.g = m.set_password(ReadExcel('admintest', 23, 6))
        time.sleep(1)
        self.h=m.emailok_btn()
    #设置https
    def test2_httpsedit(self):
        m=Configure_https(self.driver)
        n=read_files()
        text1=n[0]
        text2=n[1]
        self.a=m.set_https()
        time.sleep(1)
        self.b=m.pem_code(text1)
        self.c=m.key_code(text2)
        self.d=m.httpsok_btn()
        time.sleep(5)
    #设置用户速度
    def test3_userspeed(self):
        m=Configure_speed(self.driver)
        self.a=m.admin_advanced()
        time.sleep(1)
        self.b=m.uerupload_speed(int(ReadExcel('admintest',30,6)))
        self.c=m.userdownload_speed(int(ReadExcel('admintest',31,6)))
        self.d=m.speedok_btn()
        time.sleep(1)
        self.e=m.get_successtitle()
        time.sleep(1)
        self.assertEqual(self.e,ReadExcel('admintest',32,9))


