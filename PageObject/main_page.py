# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage
from PageObject.contact import Contact


class Main(BasePage):
    # 将父类私有属性_url重新赋值
    # _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _url = "https://www.baidu.com"

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return Contact(self._driver)

    def baidu_input(self, kw):
        self.find(By.ID, "kw").send_keys(kw)
        self.find(By.ID, "su").click()
