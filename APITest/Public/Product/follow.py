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

config = readConfig.ReadConfig()
userId = config.getUser('userId')
url = config.getUrl()

def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    # sql = 'select inquiry_id from ejet_collect_inquiry where user_id = %d' % (int(userId))
    sql = 'select product_id from ejet_public_product where user_id != %d and status  ' % (int(userId))
    connect = configDatabase.ConfigDatabase()
    # sql = "select token_id, server_type from ejet_user_separate where (token_id is not null) " \
    #       "and (user_id between 1000671 and 1001240) and server_type = 'C' and token_over_time > NOW()" \
    #       "and user_id <> 1000684"
    cursor = connect.executeSQL(sql)
    result = connect.getAll(cursor)
    connect.closeDatabase()

    # for j in range(len(result)):
    #     content['productId'] = 145
    #     content['tokenId'] = result[j][0]
    #     if result[j][1] == 'A':
    #         content['appType'] = 'A'
    #         content['packageName'] = 'com.oujia.offerplus'
    #     else:
    #         content['appType'] = 'I'
    #         content['packageName'] = 'com.Ejetsolutions.offerplus'

    for j in range(len(result)):
        content['productId'] = result[i][0]

        # 获取函数名sys._getframe().f_code.co_name
        a = requests.post(url+apiName+'.do', data=content)
        print(a.text)
    # print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'pub/product/follow')
