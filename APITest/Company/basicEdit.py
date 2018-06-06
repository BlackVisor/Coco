#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig

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

    content['companyName'] = '这是公司名1001200这是公司名1001200这是公司名1001200这是公司名1001200'
    content['country'] = 'China_86'
    content['companyAddress'] = '这是公司地址1001200'
    content['companyTel'] = '1001200'
    content['companyEmail'] = '1001200@qq.com'
    content['companyWeb'] = '这是公司网址1001200'
    content['companyProfile'] = '这是公司描述1001200'
    content['companyCity'] = '这是公司城市1001200'

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)


for i in range(1):
    apiTest(url, 'company/basic/edit')
