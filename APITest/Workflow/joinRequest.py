#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : publish.py
# @Author: Cheng JiangDong
# @Date  : 2018/5/14
# @Desc  :

import requests
from Common import queryString, configDatabase, readConfig
import json


content = queryString.QueryString.content
content["id"] = 104


# 配置接口地址
url = "http://192.168.1.50:82/offerplus/company/acceptJoin.do"

result = requests.post(url, data=content)
print(json.dumps(json.loads(result.text), ensure_ascii=False, indent=4, sort_keys=True))