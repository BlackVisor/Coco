#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import json
import random

config = readConfig.ReadConfig()
userId = config.getUser('userId')
url = config.getUrl()

def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    # connect = configDatabase.ConfigDatabase()
    # sql = 'select  from  where '
    # cursor = connect.executeSQL(sql)
    # result = connect.getAll(cursor)
    # connect.closeDatabase()

    currencyList = ['USD', 'CNY', 'EUR', 'GBP', 'CHF']
    unitList = ['PCS', 'Set', 'Box', 'Pal', 'Doz']
    validDayList = [30, 60, 90]
    priceTerms = ['FOB', 'EXW', 'FAS', 'FCA', 'CFR']
    paymentTerms = ['T/T', 'L/C', 'D/P', 'Western Union', 'Money Gram']

    for i in range(100):
        content['productName'] = '文杰的public inquiry**'+str(i)
        content['productUnit'] = random.choice(unitList)
        content['productImg'] = '2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc,2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc'
        content['productDescrip'] = '这是productDescrip'+str(i)
        content['productQuantity'] = random.randint(1,999999)
        content['expireDate'] = random.choice(validDayList)
        content['categoryId'] = random.randint(17, 150)
        content['paymentTerm'] = random.choice(paymentTerms)
        content['destinationPort'] = '这是destinationPort'
        content['priceTerm'] = random.choice(priceTerms)
        content['targetPrice'] = random.randint(1, 99999)
        content['targetPriceCry'] = random.choice(currencyList)

        # 获取函数名sys._getframe().f_code.co_name
        a = requests.post(url+apiName+'.do', data=content)
        print(a.text)
        # print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'pub/inquiry/publish')
