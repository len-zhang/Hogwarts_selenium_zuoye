# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BasePage:
    _driver = ""
    _url = ""

    def __init__(self, driver=None):
        # if driver is None:
        #     option = Options()
        #     option.debugger_address = "localhost:9222"
        #     self._driver = webdriver.Chrome(options=option)
        # else:
        #     self._driver: WebDriver = driver
        self._driver = webdriver.Remote(command_executor="http://10.0.45.32:5001/wd/hub",
                                        desired_capabilities=DesiredCapabilities.CHROME)
        if self._url != "":
            self._driver.get(self._url)
        self._driver.implicitly_wait(5)

    def find(self, by, value):  # 将业务代码与selenium剥离开，只有base.py与selenium有关联，便于以后切换其它测试框架时代码改动
        return self._driver.find_element(by=by, value=value)

    def finds(self, by, value):
        return self._driver.find_elements(by=by, value=value)

    def quit(self):
        return self._driver.quit()
