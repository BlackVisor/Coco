#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import random
import json


def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    connect = configDatabase.ConfigDatabase()

    sql = 'select offer_id from ejet_my_offer where user_id = 1001200 and offer_status = 0'
    cursor = connect.executeSQL(sql)
    result = connect.getAll(cursor)
    currencyList = ['USD', 'CNY', 'EUR', 'GBP', 'CHF']
    unitList = ['PCS', 'Set', 'Box', 'Pal', 'Doz']
    countryList = ['China_86', 'Afghanistan_93', 'Afghanistan_93', 'San Marino_378', 'Andorra_376']
    validDayList = [30, 60, 90]
    priceTerms = ['FOB', 'EXW', 'FAS', 'FCA', 'CFR']
    arraySheet = [
        {"sheetName": "MOQ", "sheetValue": "233"},
        {"sheetName": "Pcs/box", "sheetValue": "big box"},
        {"sheetName": "Delivery time", "sheetValue": "233233"},
        {"sheetName": "CBM", "sheetValue": "233233233"},
        {"sheetName": "Size", "sheetValue": "233233233233"}
    ]

    content['productId'] = result[random.randint(1,len(result))][0]
    content['categoryId'] = random.randint(1, 178)
    content['productPrice'] = random.randint(1, 999999999)/10000
    # content['productPriceCry'] = random.choice(currencyList)
    content['productPriceCry'] = 'USD'
    content['productUnit'] = random.choice(unitList)
    content['moq'] = random.randint(1, 999999)
    content['country'] = random.choice(countryList)
    content['validDay'] = random.choice(validDayList)
    content['priceTerms'] = random.choice(priceTerms)
    content['portOfShipment'] = 'this is port of shipment'
    content['productArrSheet'] = json.dumps(random.choice(arraySheet))



    # sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)


for i in range(100):
    apiTest(url, 'pub/product/publish')
