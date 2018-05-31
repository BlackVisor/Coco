import requests
from Common import readConfig
from Common.log import MyLog

localReadConfig = readConfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        global url, timeout

        protocol = localReadConfig.getHttp("protocol")
        host = localReadConfig.getHttp("url")
        port = localReadConfig.getHttp("port")
        path = localReadConfig.getHttp("appPath")
        timeout = localReadConfig.getHttp("timeout")

        self.log = MyLog.getLog()
        self.logger = self.log.logger

        self.url = None
        self.header = {}
        self.queryString = {}
        self.body = {}
        self.file = {}

    def setUrl(self):
        self.url = protocol + '://' + host + ':' +port + '/' + path + '/'

    def setHeader(self, header):
        self.header = header

    def setQueryString(self, queryString):
        self.queryString = queryString

    def setBody(self, body):
        self.body = body

    def setFile(self, file):
        self.file = file

    # define http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.queryString, headers=self.header, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # define http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.header, data=self.body, file=self.file, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
