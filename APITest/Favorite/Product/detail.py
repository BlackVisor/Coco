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

    # connect = configDatabase.ConfigDatabase()
    # sql = 'select product_id from ejet_collect_product where user_id = %d and collect_type = 2 order by rand() limit 1' % (int(userId))
    # cursor = connect.executeSQL(sql)
    # result = connect.getOne(cursor)
    # connect.closeDatabase()

    # content['productId'] = result[0]
    content['productId'] = 98669
    content['productFrom'] = 1
    # content['productId'] = 511
    # content['productFrom'] = 0

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'favorite/product/detail')
