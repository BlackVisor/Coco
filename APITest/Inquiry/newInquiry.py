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
    # sql = 'select  from  where '
    # cursor = connect.executeSQL(sql)
    # result = connect.getAll(cursor)
    # connect.closeDatabase()

    # 对来自catalog的（收藏的他人的catalog的产品或者直接去他人的catalog产品里）inquiry时需要额外传bycatalog和将offerId改为productId
    # content['bycatalog'] = '1'
    # content['productId'] = '1035'

    # 对来自received product的产品inquiry时用原来的入参
    content['offerId'] = '98669'

    content['inquiryDescrip'] = 'zheshi 98669 de inquiry'
    content['quantity'] = '800'

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)
    print(json.dumps(json.loads(a.text), ensure_ascii=False, indent=4, sort_keys=True))


for i in range(1):
    apiTest(url, 'inquiry/newInquiry')
