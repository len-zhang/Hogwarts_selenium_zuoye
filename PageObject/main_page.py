# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage
from PageObject.contact import Contact


class Main(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"  # 将父类私有属性_url重新赋值

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return Contact(self._driver)
