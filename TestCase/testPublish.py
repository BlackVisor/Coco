# -*- coding: utf-8 -*-
# @Author: Cheng JiangDon


from PageObject.LoginPage import LoginPage
import unittest
import os
from selenium import webdriver
from Public.ConfigParser import ConfigParser as config


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 在这里实例化浏览器，以保测试过程中只有一个浏览器, cls.driver会被传给继承了unittest.TestCase的类
        option = webdriver.ChromeOptions()
        __browserBinary = r'C:\Users\BlackVisor\AppData\Local\360Chrome\Chrome\Application\360chrome.exe'
        option.binary_location = __browserBinary
        option.add_argument('--disable-infobars')
        option.add_argument(r'--user-data-dir=C:\Users\BlackVisor\AppData\Local\360Chrome\Chrome\User Data')
        driverPath = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '\Driver\chromedriver.exe')
        cls.driver = webdriver.Chrome(driverPath, options=option)

    @classmethod
    def tearDownClass(cls):
        # 测试结束后清理环境，即关闭所有标签和浏览器
        cls.driver.quit()

    def setUp(self):
        # open index webpage
        LoginPage(self.driver).openUrl(config.getUrl())


    def tearDown(self):
        # close webpage
        pass

    def testLogin(self):
        LoginPage(self.driver).login()


if __name__ == "__main__":
    unittest.main()
