#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import time
import json

config = readConfig.ReadConfig()
userId = config.getUser('userId')
url = config.getUrl()


def apiTest(url, apiName):

    # for j in range(1003011, 1003030):
    #     #     content1 = queryString.QueryString.content
    #     #     # del content1['tokenId']
    #     #
    #     #     content1['loginName'] = j
    #     #     content1['password'] = 'f492a324fbf16d306ee09f5d0ac5e1eb'
    #     #     content1['serverArea'] = 'de'
    #     #     content1['timeZone'] = '+8'
    #     #     content1['osVersion'] = '11.4'
    #     #     content1['imei'] = ''
    #     #     content1['pushType'] = 1
    #     #     content1['ipAddress'] = '192.168.1.160'
    #     #     content1['mac'] = ''
    #     #     content1['electricQty'] = 58
    #     #     content1['connectType'] = ''
    #     #
    #     #     b = requests.post(url + 'login.do', data=content1)
    #     #     print(b.text)

    for h in range(1003011, 1003030):
        connect = configDatabase.ConfigDatabase()

        content = {
        'appType': 'I',
        'languagePack': 'EN',
        'packageName': 'com.Ejetsolutions.offerplus',
        'sign': '',
        'source': '0',
        'timestamp': 1000*int(time.time()),
        'version': '1.1.6',
        }
        content['country'] = 'China_86'
        content['companyName'] = '认证公司'+str(h)
        content['legalPerson'] = '我是经理'+str(h)
        content['companyTel'] = '8888-8888'
        content['companyAddress'] = '这是公司地址'+str(h)
        content['paperwork'] = '2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc，2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc'
        content['businessLicense'] = '2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc'
        content['companyCity'] = '我是城市'+str(h)
        sql2 = 'select token_id from ejet_user_separate where user_id = %d' % h
        cursor = connect.executeSQL(sql2)
        result3 = connect.getOne(cursor)
        content['tokenId'] = result3[0]


        # 获取函数名sys._getframe().f_code.co_name

        time.sleep(0.5)
        a = requests.post(url+apiName+'.do', data=content)
        print(a.text)
        c = json.loads(a.text)


        if c['status'] == '000':
            sql = 'update ejet_verify_company set verify_status = 2 where user_id = %d and verify_status = 1' % h
            connect.executeSQL(sql)
            sql1 = 'update ejet_user_company set verify_status = 2 where user_id = %d and verify_status = 1' % h
            connect.executeSQL(sql1)

for i in range(1):
    apiTest(url, 'company/verify/edit')
