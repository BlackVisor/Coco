# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Demo.py
# @Author: Cheng JiangDong
# @Date  : 2019/3/30
# @Desc  : Later equals never


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class BasePage:
    loginUrl = 'https://mail.163.com'
    def __init__(self, driver, baseUrl=loginUrl):
        self.baseUrl = baseUrl
        self.driver = driver
        self.timeout = 30

    def checkOnPage(self):
        return self.driver.current_url == (self.baseUrl + self.url)

    def _open(self, url):
        url = self.baseUrl + url
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.checkOnPage(), 'Did not sign on %s' % url

    def open(self):
        return self._open(self.url)

    def findElement(self, *location):
        return self.driver.find_element(*location)


class LoginPage(BasePage):
    url = '/'
    usernameLocation = (By.NAME, 'email')
    passwordLoacation = (By.NAME, 'password')
    submitLocation = (By.ID, 'dologin')

    def typeUsername(self, username):
        self.findElement(self.usernameLocation).send_keys(username)
    def typePassword(self, password):
        self.findElement(self.passwordLoacation).send_keys(password)
    def submit(self):
        self.findElement(self.submitLocation).click()


def testUserLogin(driver, username, password):

    loginPage = LoginPage(driver)
    loginPage.open()
    driver.switch_to.frame("x-URS-iframe")
    loginPage.typeUsername(username)
    loginPage.typePassword(password)
    loginPage.submit()


class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testCaseClass, param=None):

        testLoader = unittest.TestLoader()
        testnames = testLoader.getTestCaseNames(testCaseClass)
        suite = unittest.TestSuite()
        for name in testnames:
            # 将这个测试用例实例化后加入suite中
            suite.addTest(testCaseClass(name, param=param))
        return suite


class TestModel(ParametrizedTestCase):
    def test(self, param=None):
        self.path = param[1]
        self.argv = param[2]
        self.target = param[3]






if __name__ == '__main__':
    driver = webdriver.Edge()
    try:
        username = 'username'
        password = '123456'
        testUserLogin(driver, username, password)
        sleep(3)
        driver.switch_to.default_content()
        text = driver.find_element_by_xpath("//span[@id='spnUid']").text
        assert (text == 'username@163.com'), '用户名不匹配，登录失败！'

    finally:
        driver.close()

