# -*- coding:utf-8 -*-
from PageObject.main_page import Main


class TestSelenium:
    def setup_class(self):
        self.main = Main()  # 将Main这个类实例化

    def teardown_class(self):
        self.main.quit()

    def test_add_department(self):
        # self.main.goto_contact().add_department()
        assert "云BU" in self.main.goto_contact().get_department()
