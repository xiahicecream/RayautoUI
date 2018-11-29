#coding=utf-8
from Testcase.pagemanagement.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
class Admin_edit(BasePage):
    #点击admin头像,鼠标悬停
    def admin_click(self):
        adminclick=self.driver.find_element_by_css_selector('#admin_menu > div > div > span')
        adminclick.click()
        # ActionChains(self.driver).move_to_element(adminclick).perform()

    #编辑管理员信息
    def admin_edit(self):
        admineidt=self.driver.find_element_by_css_selector('#admin_menu > ul > li.logout > a:nth-child(2)')
        admineidt.click()

    #帐号
    def admin_account(self,adminccounts):
        adminaccount = self.driver.find_element_by_id('account')
        adminaccount.clear()
        adminaccount.send_keys(adminccounts)
    #旧密码
    def admin_old(self,adminolds):
        adminold= self.driver.find_element_by_id('old_password')
        adminold.send_keys(adminolds)
    #新密码
    def admin_new(self,adminews):
        adminew= self.driver.find_element_by_id('new_password_1')
        adminew.send_keys(adminews)
    #确认新密码
    def admin_newcom(self,adminewcoms):
        adminewcom= self.driver.find_element_by_id('new_password_2')
        adminewcom.send_keys(adminewcoms)

    # 确认按钮
    def adminok_btn(self):
        adminok= self.driver.find_element_by_id('usereditenter')
        adminok.click()

