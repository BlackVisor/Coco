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

    content['country'] = 'China_86'
    content['companyName'] = '认证公司'
    content['legalPerson'] = '我是经理'
    content['companyTel'] = '8888-8888'
    content['companyAddress'] = '这是公司地址'
    content['paperwork'] = '2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc，2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc'
    content['businessLicense'] = '2ae4f00b-0d61-4c99-aa4c-2b1f65f0defc'
    content['companyCity'] = '我是城市2'

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)


for i in range(1):
    apiTest(url, 'company/verify/edit')
