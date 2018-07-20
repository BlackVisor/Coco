#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import json
import time
from Decrypt.aesUtil import WebInEncrypt


config = readConfig.ReadConfig()
userId = config.getUser('userId')
url = config.getUrl()
# 常用各种取值列表
currencyList = ["USD", "CNY", "EUR", "GBP", "CHF", "JPY", "RUB", "INR", "CAD", "AUD", "BRL", "HKD", "TRY", "ILS", "NZD", "PKR", "SGD", "ZAR", "THB", "PHP", "MXN", "KRW", "NOK", "PLN", "IDR", "CLP", "CZK", "DKK", "HUF", "MYR", "SEK", "IQD", "RSD", "HRK", "EGP", "IRR", "AED", "SAR", "QAR", "LBP", "LYD", "JOD", "BGN", "VND", "CUP", "BOB", "COP", "DOP", "ISK", "MOP", "MAD", "TND"]
priceTermList = ["FOB", "EXW", "FAS", "FCA", "CFR", "CPT", "CIF", "CIP", "DES", "DAF", "DEQ", "DDP", "DDU"]
unitList = ["PCS", "Set", "Box", "Pal", "Doz", "Pack", "Pair", "20ft", "40ft", "40ftHQ", "g", "kg", "t", "lb", "ml", "mm", "l", "cm", "m", "Inch", "m2", "w", "v", "a"]
paymentWayList = ["T/T", "L/C", "D/P", "Western Union", "Money Gram"]



# fileName = os.path.basename(__file__)

connect = configDatabase.ConfigDatabase()

#content[''] = ''
for i in range(1003002,1003031):
    # 登录这个账号
    content0 = queryString.QueryString()
    login = content0.iosHeader.copy()
    login["loginName"] = i
    login["password"] = "f492a324fbf16d306ee09f5d0ac5e1eb"
    # login to offerplus
    toLogin = requests.post("http://192.168.1.50:82/offerplus/login.do", data=login)
    print("toLogin="+toLogin.text)
    time.sleep(1)

    # # request to join in
    # content1 = queryString.QueryString()
    # join = content1.iosHeader.copy()
    # # 1003001's companyId = 2340
    # join["tokenId"] = json.loads(toLogin.text)["data"]["tokenId"]
    # join['companyId'] = 2340
    # join['type'] = 1
    # join['authTime'] = json.loads(toLogin.text)["data"]["authTime"]
    # toJoin = requests.post("http://192.168.1.50:82/offerplus/company/joinIn.do", data = join)
    # print("toJoin="+toJoin.text)
    # time.sleep(1)
    #
    # # accept join
    # accept = {}
    # data = {}
    # accept["timestamp"] = 1000*int(time.time())
    # sql = 'select id from ejet_apply_join_company where user_id = %d order by update_time limit 1' % i
    # cursor = connect.executeSQL(sql)
    # result = connect.getOne(cursor)
    # data["id"] = result[0]
    # encrypt = WebInEncrypt()
    # encrypt.content1 = json.dumps(data)
    # accept["data"] = encrypt.encode()
    # cookies = {}
    # cookies["tokenId"] = "9db5a50f-76e9-4974-beaa-a2a24a89ba4f"
    # cookies["JSESSIONID"] = "39630A2655D709CF0D2FCB02FB05BC01"
    # toAccept = requests.post("http://192.168.1.50:82/com/account/join/accept.do", data=accept, cookies=cookies)
    # print("toAccept="+toAccept.text)
    # time.sleep(1)