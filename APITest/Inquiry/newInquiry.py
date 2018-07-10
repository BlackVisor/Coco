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

    connect = configDatabase.ConfigDatabase()
    sql = 'select product_id from ejet_category_product where user_id != %d and `status` = 0 order by rand() limit 100' % int(userId)
    cursor = connect.executeSQL(sql)
    result = connect.getAll(cursor)
    connect.closeDatabase()

    # 对来自catalog的（收藏的他人的catalog的产品或者直接去他人的catalog产品里）inquiry时需要额外传bycatalog和将offerId改为productId
    # content['bycatalog'] = '1'
    # content['productId'] = '1035'

    # 对来自received product的产品inquiry时用原来的入参
    # content['offerId'] = '98669'
    #
    # content['inquiryDescrip'] = 'zheshi 98669 de inquiry'
    # content['quantity'] = '800'

    # 直接新建inquiry的入参 type=0基于联系人，=1基于产品
    currencyList = ['USD', 'CNY', 'EUR', 'GBP', 'CHF']
    priceTerms = ['FOB', 'EXW', 'FAS', 'FCA', 'CFR']
    validDayList = [10, 20, 30, 40, 50, 60]
    unitList = ['PCS', 'Set', 'Box', 'Pal', 'Doz']
    for j in range(len(result)):
        inquiryType = random.randint(0, 1)
        content['type'] = inquiryType
        content1 = {}
        content2 = {}
        if inquiryType == 0:
            content1['contactUserId'] = '1010703'
            content1['productName'] = '直接的inquiry'+str(j)
            content1['productImg'] = 'Fr8us5eIpFOo2iyE-AHIti2I58Y_,Fr8us5eIpFOo2iyE-AHIti2I58Y_,Fr8us5eIpFOo2iyE-AHIti2I58Y_'
            content1['targetPrice'] = (random.randint(1, 999999999))/10000
            content1['targetPriceCry'] = random.choice(currencyList)
            content1['priceTerm'] = random.choice(priceTerms)
            content1['destinationPort'] = 'zheshi destinationPort '+str(j)
            content1['paymentTerm'] = 'T/T'
            content1['expireDate'] = random.choice(validDayList)
            content.update(content1)

        elif inquiryType == 1:
            content2['productId'] = result[j][0]
            content2['productSource'] = 1
            content.update(content2)
        content['inquiryDescrip'] = '这是基于产品' + str(j)
        content['productUnit'] = random.choice(unitList)
        content['productQuantity'] = random.randint(1, 999999)


        # 获取函数名sys._getframe().f_code.co_name
        a = requests.post(url+apiName+'.do', data=content)
        print(a.text)
        print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'inquiry/newInquiry')
