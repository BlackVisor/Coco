#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import random
import json
import time

config = readConfig.ReadConfig()
userId = config.getUser('userId')
url = config.getUrl()

def apiTest(url, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    # connect = configDatabase.ConfigDatabase()
    # sql = 'select offer_id from ejet_my_offer where user_id = 1001200 and offer_status = 0'
    # cursor = connect.executeSQL(sql)
    # result = connect.getAll(cursor)

    # content['categoryName'] = '第1个catalog目录'
    #
    # # 获取函数名sys._getframe().f_code.co_name
    # a = requests.post(url+apiName+'.do', data=content)
    # print(a.text)

    for j in range(30):
        content['categoryName'] = '第%d个catalog目录' % j

        # 获取函数名sys._getframe().f_code.co_name
        a = requests.post(url+apiName+'.do', data=content)
        print(a.text)

for i in range(1):
    apiTest(url, '/catalog/category/add.do')
