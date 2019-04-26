import sys
import os
import unittest
from time import sleep
from appium import webdriver



class HelloWord(unittest.TestCase):
    def testAddContact(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['patfromVersion'] = '7.0'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        desired_caps['deviceName'] = 'device'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWord)
    unittest.TextTestRunner(verbosity=2).run(suite)