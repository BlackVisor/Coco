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


def apiTest(url: str, apiName: str):

    # fileName = os.path.basename(__file__)
    content = queryString.QueryString.content
    content['companyId'] = 2340
    content['type'] = 1

    # 获取函数名sys._getframe().f_code.co_name
    # a = requests.post(url+apiName+'.do', data=content)
    # b = json.loads(a.text)
    # print(b)

    # if b['status'] == '000':
    if 1:
        # 加入成功后的影响点
        connect = configDatabase.ConfigDatabase()
        sql = 'update ejet_user eu, ejet_user_company euc, ejet_user_rela_company eurc, ejet_public_product epp, ' \
                  'ejet_public_inquiry epi, ejet_apply_join_company eajc ' \
              'set ' \
                  'eu.user_type = 2,' \
                  'eu.update_time = SYSDATE(),' \
                  'euc.used_sub_account_total = euc.used_sub_account_total + 1,' \
                  'euc.update_time = SYSDATE(),' \
                  'eurc.company_id = %d,' \
                  'eurc.access_auth = 2, ' \
                  'eurc.auth_time = SYSDATE(), ' \
                  'eurc.update_time = SYSDATE(), ' \
                  'eurc.product_total = 0, ' \
                  'eurc.used_product_total = 0, ' \
                  'epp.`status` = 4, ' \
                  'epp.update_time = SYSDATE(), ' \
                  'epi.rfq_status = 4, ' \
                  'epi.update_time = SYSDATE(), ' \
                  'eajc.`status` = 1, ' \
                  'eajc.update_time = SYSDATE()' \
              'where ' \
                  'eu.user_id = %d and eu.user_type = 0 and ' \
                  'euc.company_id = %d and ' \
                  'eurc.user_id = eu.user_id and ' \
                  'eajc.user_id = eu.user_id and eajc.`status` = 0 and ' \
                  'left join epp on epp.user_id = eu.user_id and epp.`status` in (0,2) ' \
                  'left join epi on epi.user_id = eu.user_id and epi.rfq_status in (0,2)' \
                   % (content['companyId'], int(userId), content['companyId'])

        print(sql)
        # connect.executeSQL(sql)
    else:
        print('没有加入公司成功')



for i in range(1):
    apiTest(url, 'company/joinIn.do')


