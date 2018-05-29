#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tradeOrder.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import os
import requests
import sys
from Common import queryString
from Order import getToken


def agreeUpdate(protocol, host, port, path):
    fileName = os.path.basename(__file__)
    content = queryString.QueryString().queryString()
    content['tokenId'] = getToken.GetToken.tokenId
    content['oId'] = 346802
    content['timelineOperId'] = 2194849

    a = requests.post(protocol+'://'+host+':'+port+'/'+path+'/'+fileName[:-3]+'/'+sys._getframe().f_code.co_name+'.do', data=content)
    print(a)


a = agreeUpdate('http', 'hzdev.offerplus.com', '82', 'offerplus')
