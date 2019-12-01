# -*- coding: utf-8 -*-
# @Author: Cheng JiangDong


import logging
import os.path
import time


class Logger:

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # create a handler to write log file
        logTime = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        logPath = os.path.join(os.path.dirname(os.path.abspath('.')), r'logs')
        logName = logPath + logTime + r".log"
        fileHandler = logging.FileHandler(logName)
        fileHandler.setLevel(logging.INFO)

        # create another handler to send output to console
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)

        # def handler output format
        fomatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(fomatter)
        consoleHandler.setFormatter(fomatter)

        # add handler to logger
        self.logger.addHandler(fileHandler)
        self.logger.addHandler(consoleHandler)

    def getLog(self):
        return self.logger
