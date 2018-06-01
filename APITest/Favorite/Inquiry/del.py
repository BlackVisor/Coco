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

    connect = configDatabase.ConfigDatabase()
    # sql = 'select inquiry_id from ejet_public_inquiry where user_id <> %d and rfq_status = 4 and del_status = 0' % (int(userId))
    sql = 'select id from ejet_collect_inquiry where user_id = %d' % (int(userId))
    cursor = connect.executeSQL(sql)
    result = connect.getAll(cursor)
    connect.closeDatabase()

    ids = ''
    for i in range(len(result)):
        ids = ids + str(result[i][0]) +','

    content['ids'] = ids[:-1]

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'favorite/inquiry/del')
