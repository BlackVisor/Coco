# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Entry.py
# @Author: Cheng JiangDong
# @Date  : 2019/3/30
# @Desc  : Later equals never


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
import os
import csv


class ParametrizedTestCase(unittest.TestCase):
    # 重写了TestCase的构造函数，加入了param属性
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testCaseClass, param=None):

        testLoader = unittest.TestLoader()
        testNames = testLoader.getTestCaseNames(testCaseClass)
        suite = unittest.TestSuite()
        for name in testNames:
            # 这个方法的入参是实例化后的测试类，测试类继承自unittest.TestCase, 其构造函数经过上述重写后需要两个入参
            # 将这个测试用例实例化后加入suite中,name和param对应构造函数中的两个参数
            suite.addTest(testCaseClass(name, param=param))
        return suite


class TestExecution(ParametrizedTestCase):
    def test(self, param=None):
        path = param[1]
        argv = param[2]
        name = param[3]
        caseNameList = name.strip().split(',')
        defaultCaseName = caseNameList[0]
        ret = os.system("python %s %s > %s.log 2>&1" % (path, argv, defaultCaseName))
        if ret:
            os.system("taskkill /im chromedriver.exe /F")
            os.system("taskkill /im chrome.exe /F")
        else:
            print("test execute success")


def runCase(caseList):
    suite = unittest.TestSuite()
    for case in caseList:
        suite.addTest(ParametrizedTestCase.parametrize(TestExecution, param=case))
        unittest.TextTestRunner(verbosity=2).run(suite)

def getCase():
    caseFilePath = ""
    caseList = []
    with open(caseFilePath, 'r') as f:
        fileReader = csv.reader(f)
        header = next(fileReader)
        for row in fileReader:
            if row[0] == "1":
                caseList.append(row)

        return caseList


if __name__ == '__main__':
    try:
        runCase(getCase())

    finally:
        pass

