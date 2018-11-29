#coding=utf-8
from Testcase.pagemanagement.BasePage import BasePage
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 封装首页
class LoginPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
# 使用方法输入用户名

    def set_username(self,username):
        name=self.driver.find_element_by_id('username')
        name.send_keys(username)
# 使用方法输入密码

    def set_password(self,password):
        passw=self.driver.find_element_by_id('password')
        passw.send_keys(password)
#确认登录标题

    def get_DiaglogTitle(self):
        digtitle=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-header > span')
        return digtitle.text
# 点击登录按钮

    def click(self):
        okbtn=self.driver.find_element_by_id('login_btn')
        okbtn.click()
# 用户名错误提示

    def get_errortitle(self):
        error=self.driver.find_element_by_css_selector('body > app-root > login > div > span')
        return error.text



# 密码错误提示


# 非法输入错误提示


# driver = webdriver.Chrome()
# # driver.maximize_window()#全屏
# driver.get('http://112.74.133.48:8090/admin')
# m=LoginPage(driver)
# m.set_username('admin')
# m.set_password('123456')
# m.click()
# time.sleep(2)
# # c=m.get_errortitle()
# c=m.get_DiaglogTitle()
# print c





