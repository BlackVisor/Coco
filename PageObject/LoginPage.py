# -*- coding: utf-8 -*-
# @Author: Cheng JiangDong


from PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By
from Public.ConfigParser import ConfigParser as config


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.passwordLocator = (By.CSS_SELECTOR, '#parameter')
        self.loginLocator = (By.CSS_SELECTOR, "[id='loginButton']")
        self.confirmLoginLocator = (By.CSS_SELECTOR, "[che-button-title='OK']>[type='button']")

    def login(self):
        try:
            self.findElement(*self.passwordLocator).clear()
            self.findElement(*self.passwordLocator).send_keys(config.browserConfig()['loginPassword'])
            self.waitClick(self.loginLocator)
            self.waitClick(self.confirmLoginLocator)
        except NameError as e:
            ...
