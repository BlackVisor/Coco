import time


#通用的app的请求参数
class QueryString:

    def __init__(self):
        pass

    def queryString(self):
        self.HttpHeader = {
            'appType': 'A',
            'languagePack': 'EN',
            'packageName': 'com.Ejetsolutions.offerplus',
            'sign': '',
            'source': '0',
            'timestamp': 1000*int(time.time()),
            'version': '1.1.6',
        }
        return self.HttpHeader
