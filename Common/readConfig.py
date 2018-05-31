import os
import codecs
import configparser

# 获取项目路径和配置路径
projectDirectory = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
configDirectory = os.path.join(projectDirectory, "Common", "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configDirectory)
        data = fd.read()
        self.url = ''

        # 移除BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            with codecs.open(configDirectory, "w") as file:
                file.write(data)
            file.close()
        fd.close()

        self.config = configparser.ConfigParser()
        self.config.read(configDirectory)

    def getHttp(self, name):
        value = self.config.get("http", name)
        return value

    def getDatabase(self, name):
        value = self.config.get("database", name)
        return value

    def getApp(self, name):
        value = self.config.get("app", name)
        return value

    def getUser(self, name):
        value = self.config.get("user", name)
        return value

    def getUrl(self):
        value = self.config.get("http", "protocol") + "://" + \
                self.config.get("http", "url") + ":" +\
                str(self.config.get("http", "port")) + "/" + \
                self.config.get("http", "appPath") + "/"
        return value
