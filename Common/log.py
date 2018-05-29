import logging
from datetime import datetime
import threading
import os
from Common import readConfig


class Log:
    def __init__(self):
        global logPath, resultPath, projectDirectory
        projectDirectory = readConfig.projectDirectory
        resultPath = os.path.join(projectDirectory, "Result")

        # result文件夹为空时创建此文件
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        # define test result file name by localtime
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))

        # create test result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        # define logger
        self.logger = logging.getLogger()

        # define log level
        self.logger.setLevel(logging.INFO)

        # define handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))

        # define formatter
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        # define formatter
        handler.setFormatter(formatter)

        # add handler
        self.logger.addHandler(handler)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def getLog():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log
