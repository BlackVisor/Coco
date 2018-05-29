import requests
import time


content = {
    'packageName':'com.oujia.offerplus',
    "appType": 'I',
    "version": '1.1.6',
    "languagePack": 'zh',
    "source": 1,
    "timestamp": 1000*int(time.time()),
    "tokenId": '1ce28c55-7cd4-4383-a49a-71a28ff9037f',

    'oId': 1766,


}


a = requests.post('http://hzdev.offerplus.com:82/offerplus/tradeOrder/acceptOrderBind.do', data=content)
print(a.text)