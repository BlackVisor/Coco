#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import json
import time
import random

config = readConfig.ReadConfig()
userId = config.getUser('userId')
url = config.getUrl()

def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    connect = configDatabase.ConfigDatabase()
    sql = "select token_id, server_type from ejet_user_separate where (token_id is not null) " \
          "and (user_id between 1000671 and 1001240) and server_type = 'C' and token_over_time > NOW()"
    cursor = connect.executeSQL(sql)
    result = connect.getAll(cursor)
    connect.closeDatabase()
    validDayList = [10, 20, 30, 40, 50, 60]
    currencyList = ['USD', 'CNY', 'EUR', 'GBP', 'CHF']
    unitList = ['PCS', 'Set', 'Box', 'Pal', 'Doz']
    priceTerms = ['FOB', 'EXW', 'FAS', 'FCA', 'CFR']
    for j in range(len(result)):
        content['inquiryId'] = 245
        content['tokenId'] = result[j][0]
        content['price'] = random.randint(1, 99999)
        content['priceCry'] = random.choice(currencyList)
        content['validateTime'] = random.choice(validDayList)
        content['unit'] = random.choice(unitList)
        content['priceTerms'] = random.choice(priceTerms)
        content['remarkImg'] = '2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc,2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc'
        content['placeDelivery'] = '这是placeDelivery'+str(j)
        content['remark'] = '这是remark'+str(j)
        content['deliveryTime'] = str(random.randint(1,30))
        if result[i][1] == 'A':
            content['appType'] = 'A'
            content['packageName'] = 'com.oujia.offerplus'
        else:
            content['appType'] = 'I'
            content['packageName'] = 'com.Ejetsolutions.offerplus'

        # 获取函数名sys._getframe().f_code.co_name
        a = requests.post(url+apiName+'.do', data=content)
        print(a.text)
    # print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'pub/inquiry/simpleQuota')
