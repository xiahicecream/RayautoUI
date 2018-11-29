#coding=utf-8
from Testcase.pagemanagement.BasePage import BasePage
#封装Raysyncserver页面

class Serverpage(BasePage):
#服务器关闭按钮
    def shutdown_btn(self):
        shutdown=self.driver.find_element_by_id('shutdown_btn')
        shutdown.click()

#服务器重启按钮
    def restart_btn(self):
        restart=self.driver.find_element_by_id('restart_btn')
        restart.click()

#服务器启动按钮
    def start_btn(self):
        start=self.driver.find_element_by_id('start_btn')
        start.click()
#点击基础信息编辑按钮
    def edition_btn(self):
        edition=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > server-info > div.server_info_body > div.main_infos > div.base_infos > p > i')
        edition.click()
#服务器地址输入框
    def host_edit(self,host):
        hosts=self.driver.find_element_by_css_selector('body > nz-modal > div > div.ant-modal-wrap > div.ant-modal > div > div.ant-modal-body > div > div > div:nth-child(2) > input')
        hosts.clear()
        hosts.send_keys(host)

#服务器输入激活码
    def license_edit(self,license):
       licenses=self.driver.find_element_by_css_selector('body > nz-modal > div > div.ant-modal-wrap > div.ant-modal > div > div.ant-modal-body > div > div > div:nth-child(8) > input')
       licenses.clear()
       licenses.send_keys(license)

#编辑服务器ok按钮
    def edit_ok(self):
        edit_btn=self.driver.find_element_by_css_selector('body > nz-modal > div > div.ant-modal-wrap > div.ant-modal > div > div.ant-modal-footer > div > button:nth-child(2)')
        edit_btn.click()

#确认重启服务器按钮
    def confirm_btn(self):
        confirms=self.driver.find_element_by_css_selector('body > nz-modal > div > div.ant-modal-wrap > div.ant-modal > div > div.ant-modal-footer > button.ant-btn.ant-btn-primary.ant-btn-lg > span')
        confirms.click()

#license激活信息
    def license_titles(self):
        license_title=self.driver.find_element_by_css_selector('body > app-root > home > nz-layout > nz-content > nz-layout > nz-content > nz-content > server-info > div.server_info_body > div.snapshot > div.header > div.server_info_snapshot > nz-popover > p > span:nth-child(2)')
        return license_title.text

#判断元素是否存在，用来判断服务器运行状态是正常运行还是未运行，因该元素是随机生成因此判断前方图标是否存在。
    def is_ElementExist(self,element):
        flag=True
        try:
            self.driver.find_element_by_css_selector(element)
            return flag
        except:
            flag=False
            return flag







