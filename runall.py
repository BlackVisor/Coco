import os
import unittest
import HtmlTestRunner
from Common import readConfig
from Common.log import MyLog


def setCaseList(self):
    fb = open(self.caselistfile)
    for value in fb.readlines():
        data = str(value)
        if data != '' and not data.startswith("#"):
            self.caselist.append(data.replace("\n", ""))
    fb.close()


def setCaseSuite(self):
    self.setCaseList()
    testSuite = unittest.TestSuite()
    suiteModel = []

    for case in self.caselist:
        caseFile = os.path.join(readConfig.projectDirectory, "TestCase")
        print(caseFile)
        caseName = case.split("/")[-1]
        print(caseName+".py")
        discover = unittest.defaultTestLoader.discover(caseFile, pattern=caseName+'.py', top_level_dir=None)
        suiteModel.append(discover)

    if len(suiteModel) > 0:
        for suite in suiteModel:
            for test_name in suite:
                testSuite.addTest(test_name)

    else:
        return None
    return testSuite


def run(self):
    try:
        log = MyLog.getLog()
        logger = log.logger
        suit = self.setCaseSuite()
        if suit is not None:
            logger.info("********TEST START********")
            fp = open(resultpath,'wb')
            runner = HtmlTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description='Test Description')
            runner.run(suit)
        else:
            logger.info("Have no case to test.")
    except Exception as ex:
        logger.error(str(ex))
    finally:
        logger.info("********TEST END********")
        # # send test report by email
        # if int(on_off) ==0:
        #     self.email.send.email()
        # elif ini(on_off) ==1:
        #     logger.info("Doesn't send report email to developer.")
        # else:
        #     logger.info("Unkown state")