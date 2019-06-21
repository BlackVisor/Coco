# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : BasePage.py
# @Author: Cheng JiangDong
# @Date  : 2019/4/3
# @Desc  : Later equals never


import os
import sys
import time
from selenium import webdriver


class BasePage:
    """
        定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self, driver):
        self.driver = driver

    # 关闭浏览器
    def quitBrowser(self):
        self.driver.quit()

    def findElement(self, *locator):
        return self.driver.find_element(*locator)

    def findElements(self, *locator):
        return self.driver.find_elements(*locator)

    @classmethod
    def setUpClass(cls):
        # 在这里实例化浏览器，以保测试过程中只有一个浏览器
        option = webdriver.ChromeOptions()
        option.add_argument("disable-infobars")
        driverPath = os.path.dirname(os.path.dirname(__file__)) + '/Driver/chromedriver.exe'
        cls.driver = webdriver.Chrome(driverPath, options=option)

    @classmethod
    def tearDownClass(cls):
        # 测试结束后清理环境，即关闭所有标签和浏览器
        cls.driver.close()

    @staticmethod
    def sleep(seconds: int):
        time.sleep(seconds)
