#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import json
from datetime import datetime
import random


config = readConfig.ReadConfig()
userId = config.getUser('userId')
url = config.getUrl()
time = datetime.now()

def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    # connect = configDatabase.ConfigDatabase()
    # sql = 'select  from  where '
    # cursor = connect.executeSQL(sql)
    # result = connect.getAll(cursor)
    # connect.closeDatabase()

    content['outTradeNo'] = c['data']['orderId']
    content['tradeNo'] = str(userId)+'18'+datetime.strftime(time, '%m%d%H%M%S')

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))

for i in range(1):
    # 获取outTradeNo
    content1 = queryString.QueryString.content
    # 0首充 1续费 2额外包
    aa = random.randint(1, 1)
    ab = random.randint(0, 0)
    if aa == 0:
        apiName = 'pay/alipay'
    elif aa == 1:
        apiName = 'pay/wechatPay'
    elif aa == 2:
        apiName = 'pay/paypalToken'
    elif aa == 3:
        apiName = 'pay/creditToken'

    if ab == 1:
        content1['type'] = 1
        content1['subAccountTotal'] = random.randint(0, 10)
        content1['productTotal'] = random.randint(0, 10)
    else:
        content1['type'] = 2
        content1['subAccountTotal'] = random.randint(100, 100)
        content1['productTotal'] = random.randint(100, 100)

    # 首充
    content1['type'] = 0
    content1['subAccountTotal'] = random.randint(0, 10)
    content1['productTotal'] = random.randint(0, 10)

    b = requests.post(url+apiName+'.do', data=content1)
    print(b.text)
    c = json.loads(b.text)

    apiTest(url, 'pay/publicNotify')