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

    content['companyPhotos'] = 'Fnwlvyuxikjd-DGnuKoydD7IeHI1,FiwLqwNj1f6OOGISk27ds_En7-g5,FvVZQ19O_LcSaJdguUkvfsIe_mtx,Fl8Bgpm18HDKRHrMoYymzFlu_uGc,Fkj5cHlk3HTqd4_mapQF1S8LaFDX,FiYVc2sXGH5J0_-GHqbAbuclLC1d,FmZ9PqbaYqO8ry1xCrJ9Z7Lcm-C9'

    # 获取函数名sys._getframe().f_code.co_name
    a = requests.post(url+apiName+'.do', data=content)
    print(a.text)


for i in range(1):
    apiTest(url, 'company/editGallery')
