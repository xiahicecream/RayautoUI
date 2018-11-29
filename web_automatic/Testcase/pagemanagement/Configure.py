#coding=utf-8
from Testcase.pagemanagement.BasePage import BasePage
class Configure_email(BasePage):
#点击邮箱设置
    def set_email(self):
        emails=self.driver.find_element_by_id('admin_mail_info')
        emails.click()
#设置发件人昵称
    def set_nickname(self,nickname):
        nicknames=self.driver.find_element_by_css_selector('#email > ul > li:nth-child(1) > input')
        nicknames.clear()
        nicknames.send_keys(nickname)

#设置发件人邮箱
    def set_fromemail(self,fromemail):
        fromemails=self.driver.find_element_by_css_selector('#email > ul > li:nth-child(2) > input')
        fromemails.clear()
        fromemails.send_keys(fromemail)

#设置SMTPhost
    def set_smtphost(self,smtphost):
        smtphosts = self.driver.find_element_by_css_selector('#email > ul > li:nth-child(3) > input')
        smtphosts.clear()
        smtphosts.send_keys(smtphost)

#设置SMTPPORT
    def set_smtpport(self,smtpport):
        smtpports = self.driver.find_element_by_css_selector('#email > ul > li:nth-child(4) > input')
        smtpports.clear()
        smtpports.send_keys(smtpport)

#设置SMTP帐号
    def set_smtpaccount(self,smtpaccount):
        smtpaccounts=self.driver.find_element_by_css_selector('#email > ul > li:nth-child(6) > input')
        smtpaccounts.clear()
        smtpaccounts.send_keys(smtpaccount)

#设置密码
    def set_password(self,password):
        passwords=self.driver.find_element_by_css_selector('#email > ul > li:nth-child(7) > input')
        passwords.clear()
        passwords.send_keys(password)
#点击确定按钮
    def emailok_btn(self):
        emailoks=self.driver.find_element_by_id('updateEmailBtn')
        emailoks.click()

class Configure_https(BasePage):
    #点击https证书标签栏
    def set_https(self):
        set_http=self.driver.find_element_by_id('admin_changepassword')
        set_http.click()
    #上传证书文件
    def pem_code(self,pemcode):
        pem_codes=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > https > div:nth-child(3) > textarea')
        pem_codes.send_keys(pemcode)
    #上传密钥
    def key_code(self,keycode):
        key_codes=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > https > div:nth-child(4) > textarea')
        key_codes.send_keys(keycode)
    #确定按钮
    def httpsok_btn(self):
        httpsok=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > https > div:nth-child(5) > button')
        httpsok.click()


class Configure_speed(BasePage):
    #点击高级设置标签栏
    def admin_advanced(self):
        admin_advanced=self.driver.find_element_by_id('admin_advanced')
        admin_advanced.click()
    #设置用户上传速度
    def uerupload_speed(self,userupload):
        useruploads=self.driver.find_element_by_id('uploadSpeed')
        useruploads.clear()
        useruploads.send_keys(userupload)
    # 设置用户下载速度
    def userdownload_speed(self, download):
        userdowns = self.driver.find_element_by_id('downloadSpeed')
        userdowns.clear()
        userdowns.send_keys(download)
    #确定按钮
    def speedok_btn(self):
        speedok=self.driver.find_element_by_id('updateCdn')
        speedok.click()
    #设置成功标签
    def get_successtitle(self):
        successtitle=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > advanced > p')
        return successtitle.text
