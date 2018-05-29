#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : apiTest.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString


def apiTest(protocol, host, port, path, apiName):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content




    # content['companyPhotots'] = 'FhdEOliuacm7qVYlyBkKXi9HVXxz,FhdEOliuacm7qVYlyBkKXi9HVXxz'
    content['oId'] = 859346



    # sys._getframe().f_code.co_name
    a = requests.post(protocol+'://'+host+':'+port+'/'+path+'/'+apiName+'.do', data=content)
    print(a.text)


apiTest('http', 'hzdev.offerplus.com', '82', 'offerplus', 'tradeOrder/detail')
