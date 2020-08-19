# -*- coding:utf-8 -*-
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope="module")
def get_cookie():
    option = Options()
    option.debugger_address = "localhost:9222"
    driver = webdriver.Chrome(options=option)  # 将复用浏览器的driver赋值给driver，后面用driver.的时候才会在复用浏览器里执行操作
    cookies = driver.get_cookies()  # 在复用浏览器的当前页面中获取cookie，返回的是个list
    for cookie in cookies:
        if 'expiry' in cookie.keys():
            cookie.pop('expiry')
    print("这是个fixture，在module中执行一次")
    yield cookies

# def test_cookie(get_cookie):
#     print(get_cookie)
