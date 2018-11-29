from selenium import webdriver
import unittest
import time
from Testcase.pagemanagement.LoginPage import LoginPage
from Testcase.models.driver import adminurl

class MyTest(unittest.TestCase):
    def setUp(self):
        self.url=adminurl()
        self.driver=webdriver.Chrome()
        self.driver.get(self.url)
        # self.driver.maximize_window()
        time.sleep(2)
        m=LoginPage(self.driver)
        m.set_username('admin')
        m.set_password('Raysync@123')
        m.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
