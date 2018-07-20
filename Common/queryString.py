import time
from Common import getToken


# 通用的app的请求参数
class QueryString:

    def __init__(self):
        pass

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
    content={}
    if appType == 'A':
        content = androidHeader.copy()
    else:
        content = iosHeader.copy()

    content['tokenId'] = token.token_id