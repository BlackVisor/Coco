#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase
import json


def apiTest(protocol, host, port, path, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content

    # connect = configDatabase.ConfigDatabase()
    # sql = 'select  from  where '
    # cursor = connect.executeSQL(sql)
    # result = connect.getAll(cursor)
    # connect.closeDatabase()

    #content[''] = ''

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(protocol+'://'+host+':'+port+'/'+path+'/'+apiName+'.do', data=content)
    print(a.text)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest('http', 'hzdev.offerplus.com', '82', 'offerplus', 'favorite/inquiry/detail')
