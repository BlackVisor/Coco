import time
from Common import getToken


#通用的app的请求参数
class QueryString:

    def __init__(self):
        self.iosHeader = ''
        self.androidHeader = ''
        self.content = {}

    iosHeader = {
        'appType': 'I',
        'languagePack': 'EN',
        'packageName': 'com.Ejetsolutions.offerplus',
        'sign': '',
        'source': '0',
        'timestamp': 1000*int(time.time()),
        'version': '1.1.6',
    }

    androidHeader = {
        'appType': 'A',
        'languagePack': 'EN',
        'packageName': 'com.oujia.offerplus',
        'sign': '',
        'source': '0',
        'timestamp': 1000 * int(time.time()),
        'version': '1.1.6',
    }

    token = getToken.GetToken()
    appType = token.app_type
    if appType == 'A':
        content = androidHeader
    else:
        content = iosHeader

    content['tokenId'] = token.token_id
