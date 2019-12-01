# -*- coding: utf-8 -*-
# @Author: Cheng JiangDong


import json
import os


class ConfigParser:

    configFile = os.path.dirname(os.path.dirname(__file__)) + "/config.json"
    with open(configFile, "r") as f:
        config = json.loads(f.read())

    @classmethod
    def browserConfig(cls):
        return cls.config["browserConfig"]

    @classmethod
    def AIHostConfig(cls):
        return cls.config["AIHostConfig"]

    @classmethod
    def getUrl(cls):
        return cls.config["browserConfig"]["httpType"] + r"://" + cls.config["browserConfig"]["host"] + r":" +\
               cls.config["browserConfig"]["port"]
