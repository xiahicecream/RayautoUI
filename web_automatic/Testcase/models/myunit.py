from selenium import webdriver
import unittest
from Testcase.models.driver import adminurl,nweurl
class MyTest(unittest.TestCase):
    def setUp(self):
        self.url=adminurl()
        self.driver=webdriver.Chrome()
        self.driver.get(self.url)
        # self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
# unittest.main()

class Mytestnew(unittest.TestCase):
    def setUp(self):
        self.url=nweurl()
        self.driver=webdriver.Chrome()
        self.driver.get(self.url)
        # self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()


