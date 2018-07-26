#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import json

config = readConfig.ReadConfig()
userId = config.getUser('userId')
url = config.getUrl()
# 常用各种取值列表
currencyList = ["USD", "CNY", "EUR", "GBP", "CHF", "JPY", "RUB", "INR", "CAD", "AUD", "BRL", "HKD", "TRY", "ILS", "NZD", "PKR", "SGD", "ZAR", "THB", "PHP", "MXN", "KRW", "NOK", "PLN", "IDR", "CLP", "CZK", "DKK", "HUF", "MYR", "SEK", "IQD", "RSD", "HRK", "EGP", "IRR", "AED", "SAR", "QAR", "LBP", "LYD", "JOD", "BGN", "VND", "CUP", "BOB", "COP", "DOP", "ISK", "MOP", "MAD", "TND"]
priceTermList = ["FOB", "EXW", "FAS", "FCA", "CFR", "CPT", "CIF", "CIP", "DES", "DAF", "DEQ", "DDP", "DDU"]
unitList = ["PCS", "Set", "Box", "Pal", "Doz", "Pack", "Pair", "20ft", "40ft", "40ftHQ", "g", "kg", "t", "lb", "ml", "mm", "l", "cm", "m", "Inch", "m2", "w", "v", "a"]
paymentWayList = ["T/T", "L/C", "D/P", "Western Union", "Money Gram"]

def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    # connect = configDatabase.ConfigDatabase()
    # sql = 'select  from  where '
    # cursor = connect.executeSQL(sql)
    # result = connect.getAll(cursor)
    # connect.closeDatabase()

    content['offerId'] = 98704

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'receOfferInfo')
