# -*- coding:utf-8 -*-
import os
import shelve
from selenium import webdriver
from selenium.webdriver.common.by import By

root_path = os.path.dirname(__file__)


class TestWechat:

    def setup_method(self):
        self.driver = webdriver.Chrome()  # 在方法setup中重新赋值一个实例属性self.driver，新开一个浏览器的driver
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(5)  # 隐式等待
        print("这是个测试方法setup，在每个测试方法前执行")

    def teardown_method(self):
        print("这是个测试方法teardown，在每个测试方法后执行")
        self.driver.quit()  # 关闭新开的浏览器

    def test_wechat(self, get_cookie):  # 参数传入了fixture函数，可以直接用fixture函数的返回值
        db = shelve.open(root_path + "\\mydb\\wechatcookies")  # shelve是个小型数据库，对象持久化保存数据
        db['cookie'] = get_cookie
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")  # 打开目标网页
        for c in cookies:
            self.driver.add_cookie(c)  # 把存在db里的cookie添加到打开网页的cookie中
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")  # 再次打开目标网页
        self.driver.find_element(by=By.ID, value="menu_contacts").click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(by=By.ID, value="js_upload_file_input").send_keys("D:\\test.xlsx")
        result = self.driver.find_element(by=By.ID, value="upload_file_name").text  # 通过.text获取元素的名字
        assert result == "test.xlsx"
