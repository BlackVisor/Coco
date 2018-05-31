#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import json


def apiTest(protocol, host, port, path, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    content = queryString.QueryString.content
    user = readConfig.ReadConfig()
    userId = user.getUser('userId')

    connect = configDatabase.ConfigDatabase()
    sql = 'select product_id from ejet_category_product where user_id != %d and status = 0' % (int(userId))
    cursor = connect.executeSQL(sql)
    result = connect.getOne(cursor)
    connect.closeDatabase()

    content['productId'] = result[0]

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(protocol+'://'+host+':'+port+'/'+path+'/'+apiName+'.do', data=content)
    print(a.text)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest('http', 'hzdev.offerplus.com', '82', 'offerplus', 'favorite/product/del')
