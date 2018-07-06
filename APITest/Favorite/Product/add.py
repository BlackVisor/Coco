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

    connect = configDatabase.ConfigDatabase()
    # sql = 'select product_id from ejet_category_product where user_id != %d and status = 0 limit 200' % (int(userId))
    sql = 'select offer_id from ejet_my_rece_rela where user_id = %d and del_status = 0 order by update_time desc limit 1' % (int(userId))
    cursor = connect.executeSQL(sql)
    result = connect.getAll(cursor)
    connect.closeDatabase()

    # for j in range(len(result)):
    for j in range(1):
    #     content['productId'] = result[j][0]
        content['productId'] = 257
        # type is: 0=from catalog, 1=from received product
        content['type'] = 0

        time.sleep(0.5)

        # 获取函数名sys._getframe().f_code.co_name
        a = requests.post(url+apiName+'.do', data=content)
        print(a.text)
        # print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'favorite/product/add')
