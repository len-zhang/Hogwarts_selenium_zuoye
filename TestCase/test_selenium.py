# -*- coding:utf-8 -*-
import time
import multiprocessing
import pytest

from PageObject.main_page import Main


class TestSelenium:
    # def setup_class(self):
    #     self.main = Main()  # 将Main这个类实例化
    #     print("这是在跑setup_class")
    #
    # def teardown_class(self):
    #     self.main.quit()
    #     print("这是在跑teardown_class")
    #
    # def test_add_department(self):
    #     # self.main.goto_contact().add_department()
    #     assert "云BU" in self.main.goto_contact().get_department()

    def test_baidu1(self):
        self.main = Main()
        self.main.baidu_input("hogwarts")
        time.sleep(2)
        self.main.quit()
        assert 1 == 1

    def test_baidu2(self):
        self.main = Main()
        self.main.baidu_input("hello word")
        time.sleep(4)
        self.main.quit()
        assert 1 == 1

    def test_baidu3(self):
        self.main = Main()
        self.main.baidu_input("python")
        time.sleep(6)
        self.main.quit()
        assert 1 == 1


def run(case_name):
    pytest.main([f"test_selenium.py::TestSelenium::{case_name}", "-v", "-s"])


if __name__ == '__main__':
    name_list = ["test_baidu1", "test_baidu2", "test_baidu3"]
    # pytest.main(["test_selenium.py::TestSelenium::test_baidu2", "-v", "-s"])
    pool = multiprocessing.Pool(3)
    pool.map(run, name_list)
    pool.close()
    pool.join()
