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

def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    config = readConfig.ReadConfig()
    userId = config.getUser('userId')

    connect = configDatabase.ConfigDatabase()
    sql = 'select offer_id from ejet_my_offer where user_id = %d and offer_status = 0 order by rand() limit 200' % (int(userId))
    cursor = connect.executeSQL(sql)
    result = connect.getAll(cursor)
    connect.closeDatabase()

    sql1 = 'select id from ejet_user_category where user_id  = 1001200 order by rand() limit 1'
    cursor1 = connect.executeSQL(sql1)
    result1 = connect.getOne(cursor1)

    ids = ''
    for i in range(len(result)):
        ids = ids + str(result[i][0]) + ','

    ids = ids[:-1]
    # content['categoryId'] = result1[0]
    content['categoryId'] = 84
    content['ids'] = ids

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'catalog/category/product/add')
