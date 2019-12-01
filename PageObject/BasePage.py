# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : BasePage.py
# @Author: Cheng JiangDong
# @Date  : 2019/4/3
# @Desc  : Later equals never


import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

    def waitVisible(self, locator, timeout: int = 10, frequency: float = 0.5):
        return WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(locator))

    def waitNotVisible(self, locator, timeout: int = 10, frequency: float = 0.5):
        return WebDriverWait(self.driver, timeout, frequency).until_not(EC.visibility_of_element_located(locator))

    def waitClick(self, locator, timeout: int = 10, frequency: float = 0.5):
        self.waitVisible(locator, timeout, frequency)
        # 下面的入参locator前面必须有*，这样findElement接受参数时才能直接接受该参数，而不是重新拼成tuple
        # 直接用click()会失效，所以用调用js的方式点击
        self.driver.execute_script("arguments[0].click();", self.findElement(*locator))

    def openUrl(self, url: str):
        self.driver.get(url)
        self.passwordLocator = (By.CSS_SELECTOR, '#parameter')
        self.waitVisible(self.passwordLocator)

    @staticmethod
    def sleep(seconds: int):
        time.sleep(seconds)
