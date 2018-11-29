#coding=utf-8
from Testcase.pagemanagement.BasePage import BasePage
import time
from selenium import webdriver

# 封装添加用户页面
class Userddpage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
# 使用方法输入昵称

    def set_username(self,username):
        name=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(1) > input')
        name.send_keys(username)
# 使用方法输入账号

    def set_account(self,account):
        acct=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(2) > input')
        acct.send_keys(account)

# 使用方法输入密码

    def set_password(self,password):
        passw = self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(3) > input')
        passw.clear()
        passw.send_keys(password)

# 使用方法输入用户主目录
    def set_catalogue(self,catalogue):
        catalogus=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(4) > input')
        catalogus.send_keys(catalogue)

#使用方法设置权限
    def set_rights(self):
        right=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(5) > label:nth-child(3) > input')
        right.click()

#使用方法限制上传速度
    def set_uploads(self,upload_speed):
        uploads=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(6) > input:nth-child(2)')
        uploads.send_keys(upload_speed)

#使用方法限制下载速度
    def set_downloads(self,download_speed):
        downloads=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(6) > input:nth-child(4)')
        downloads.send_keys(download_speed)

# # 使用方法输入Email
#
#     def set_email(self,email):
#         ema = self.driver.find_element_by_css_selector(
#             'body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(7) > input')
#         ema.send_keys(email)

# # 使用方法输入电话号码
#     def set_phonenumber(self,phonenumber):
#         pho = self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(8) > input')
#         pho.send_keys(phonenumber)

    # # 使用方法输入公司名称
    # def set_companyName(self,companyName):
    #     com = self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(9) > input')
    #     com.send_keys(companyName)

    # # 使用方法输入地址
    # def set_address(self,address):
    #     add = self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(10) > input')
    #     add.send_keys(address)

    # 使用方法输入备注

    def set_remark(self,remark):
        rem = self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > page-user-edit > section.content > div > div > div > div.box-body > div:nth-child(11) > input')
        rem.send_keys(remark)
    #点击确定按钮
    def set_click(self):
        cli=self.driver.find_element_by_id('usereditenter')
        cli.click()
    #返回成功提示
    def get_normaltitle(self):
        normal = self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > users > div.users_header.pages_header > h4').text
        return normal

    #删除用户，点击删除按钮
    def del_user(self):
        del_users = self.driver.find_element_by_id('userdel')
        del_users.click()

    #点击删除，确认按钮
    def del_confirm(self):
        confirm=self.driver.find_element_by_css_selector('body > nz-modal > div > div.ant-modal-wrap > div.ant-modal > div > div.ant-modal-footer > button.ant-btn.ant-btn-primary.ant-btn-lg')
        confirm.click()









