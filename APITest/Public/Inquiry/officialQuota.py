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
    sql = "select token_id, server_type from ejet_user_separate eus left join ejet_user_company euc on euc.user_id = eus.user_id where (eus.token_id is not null) and (eus.user_id between 1000671 and 1001240) and eus.server_type = 'C' and eus.token_over_time > NOW() and eus.user_id <> 1000690 and euc.verify_status = 2"
    cursor = connect.executeSQL(sql)
    result = connect.getAll(cursor)
    connect.closeDatabase()
    validDayList = [10, 20, 30, 40, 50, 60]
    currencyList = ['USD', 'CNY', 'EUR', 'GBP', 'CHF']
    unitList = ['PCS', 'Set', 'Box', 'Pal', 'Doz']
    priceTerms = ['FOB', 'EXW', 'FAS', 'FCA', 'CFR']
    paymentTerms = ['T/T', 'L/C', 'D/P', 'Western Union', 'Money Gram']

    for j in range(len(result)):
        content['inquiryId'] = 145
        content['tokenId'] = result[j][0]
        content['products'] = '[{"productName":"zheshi chanpin mingzi ", \
                               "productImg":"1be3c349-8a94-4663-bb1e-e58a180a1f6f,224dc4b8-6c1a-4cd4-b6d7-9797ef99d898", \
                               "productQuantity":666, \
                               "productPrice":654.454 \
                               "productPriceCry":"USD" \
                               "productUnit":"Box" \
                               "remark":"this is remark" \
                               "productArrSheet":[{"sheetName":"MOQ","sheetValue":"1"},{"sheetName":"Pcs/box","sheetValue":"1"},{"sheetName":"Delivery time","sheetValue":"1"},{"sheetName":"CBM","sheetValue":"1"},{"sheetName":"Size","sheetValue":"1"}] \
                               "remarkImg":"1be3c349-8a94-4663-bb1e-e58a180a1f6f,1be3c349-8a94-4663-bb1e-e58a180a1f6f" \
                              },{"productName":"zheshi chanpin mingzi1 ", \
                               "productImg":"1be3c349-8a94-4663-bb1e-e58a180a1f6f,224dc4b8-6c1a-4cd4-b6d7-9797ef99d898", \
                               "productQuantity":666, \
                               "productPrice":654.454 \
                               "productPriceCry":"USD" \
                               "productUnit":"Box" \
                               "remark":"this is remark" \
                               "productArrSheet":[{"sheetName":"MOQ","sheetValue":"1"},{"sheetName":"Pcs/box","sheetValue":"1"},{"sheetName":"Delivery time","sheetValue":"1"},{"sheetName":"CBM","sheetValue":"1"},{"sheetName":"Size","sheetValue":"1"}] \
                               "remarkImg":"1be3c349-8a94-4663-bb1e-e58a180a1f6f,1be3c349-8a94-4663-bb1e-e58a180a1f6f" \
                              }]'

        content['validateTime'] = random.choice(validDayList)
        content['unit'] = random.choice(unitList)
        content['tradeTerms'] = '["it is trade term 1", "it is trade term 2", "it is trade term 3"]'
        content['bankAccount'] = '2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc,2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc'
        content['otherFees'] =  '[{"fees":"trans","price":200.03},{"fees":"eat","price":420.03},{"fees":"shop","price":240.05}]'
        content['priceTerms'] = random.choice(priceTerms)
        content['paymentWay'] = random.choice(paymentTerms)
        content['remarkImg'] = '2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc,2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc,2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc '
        content['placeDelivery'] = 'this is place of delivery'+str(j)
        content['remark'] = 'this is reamrk'+str(j)
        content['deliveryTime'] = str(random.randint(1, 30))
        # if result[i][1] == 'A':
        #     content['appType'] = 'A'
        #     content['packageName'] = 'com.oujia.offerplus'
        # else:
        #     content['appType'] = 'I'
        #     content['packageName'] = 'com.Ejetsolutions.offerplus'

        # 获取函数名sys._getframe().f_code.co_name
        a = requests.post(url+apiName+'.do', data=content)
        print(a.text)
    # print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'pub/inquiry/officialQuota')
