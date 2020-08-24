# -*- coding:utf-8 -*-
import time
from selenium.webdriver.common.by import By

from PageObject.base_page import BasePage


class Contact(BasePage):
    def goto_add_department(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        time.sleep(2)
        self.find(By.NAME, "name").send_keys("云BU")
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR, ".qui_dialog_body [id='1688850313586212_anchor']").click()
        self.find(By.CSS_SELECTOR, "[d_ck='submit']").click()

    def get_department(self):
        a = self.finds(By.ID, "1688850316579321_anchor")
        # department_list = [i.text for i in origin_list]
        # print(department_list)
        return a[0].text
