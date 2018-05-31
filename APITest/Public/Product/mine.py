#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import json


def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    # connect = configDatabase.ConfigDatabase()
    # sql = 'select offer_id from ejet_my_offer where user_id = 1001200 and offer_status = 0'
    # cursor = connect.executeSQL(sql)
    # result = connect.getAll(cursor)

    content['page'] = 1
    content['pageNum'] = 20
    content['searchName'] = ''
    # content['status'] =

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'pub/product/mine')
