from Common import queryString
import requests, time


for j in range(1003011, 1003030):
    content1 = {
        'appType': 'I',
        'languagePack': 'EN',
        'packageName': 'com.Ejetsolutions.offerplus',
        'sign': '',
        'source': '0',
        'timestamp': 1000*int(time.time()),
        'version': '1.1.6',
    }

    content1['loginName'] = j
    content1['password'] = 'f492a324fbf16d306ee09f5d0ac5e1eb'
    content1['serverArea'] = 'de'
    content1['timeZone'] = '+8'
    content1['osVersion'] = '11.4'
    content1['imei'] = ''
    content1['pushType'] = 1
    content1['ipAddress'] = '192.168.1.160'
    content1['mac'] = ''
    content1['electricQty'] = 58
    content1['connectType'] = ''

    b = requests.post('http://hzdev.offerplus.com:82/offerplus/login.do', data=content1)
    print(b.text)