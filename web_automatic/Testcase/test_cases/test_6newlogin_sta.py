# coding=utf-8
import time
from data import ReadExcel


from Testcase.models.myunit import Mytestnew
from Testcase.pagemanagement.LoginPage import LoginPage


class New_login(Mytestnew):
    def test1_newlogin(self):
        m=LoginPage(self.driver)
        self.a=m.set_username(ReadExcel('admintest',35,6))
        self.b=m.set_password(ReadExcel('admintest',37,6))
        self.c=m.click()
        time.sleep(4)
        self.d=m.get_DiaglogTitle()
        self.assertEqual(self.d,ReadExcel('admintest',10,9))





