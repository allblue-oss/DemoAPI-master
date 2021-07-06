#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/17 15:19
# @Author : 杜云慧
# @Site : 
# @File : RSA_encrypt_sign.py
# @Software: PyCharm

import json
import requests
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA1
import base64
from config import setting
# from API_TEST_FEAME.common.localconfig_utils import local_config
# from common.localconfig_utils import local_config
from lib.readexcel import ReadExcel


def rsa_sign(message):
    msg = message.encode('utf-8')
    private_key = RSA.importKey(
        ('-----BEGIN RSA PRIVATE KEY-----\n' + setting.TEST_ENVIRONMENT_KEY + '\n-----END RSA PRIVATE KEY-----').encode(
            'utf-8'))
    # private_key = RSA.importKey(key)
    ## message做“哈希”处理，RSA签名这么要求的
    hash_obj = SHA1.new(msg)
    signature = PKCS1_v1_5.new(private_key).sign(hash_obj)
    return base64.b64encode(signature)


# data = {'module': '网支测试环境接口', 'ID': 'wangzhiapi_balancequery_001', 'UseCase': '测试环境商户余额查询接口', 'url': 'https://test_nucc.bhecard.com:9088/api_gateway.do', 'method': 'post', 'params': '', 'headers': '', 'body': '{"sign": "sign", "charset": "UTF-8", "biz_content":{"merchant_id":"900029000000354"},"partner": "900029000000354", "sign_type": "RSA", "service": "trade.acc.balance"}', 'type': '', 'resultcode': '00', 'msg': 'BUSINESS_OK', 'result': '', ' testers': ''}
# body = eval(data['body'])
# biz_content_read = eval(data['body'])['biz_content']
# biz_content = json.dumps(biz_content_read)
# sign = rsa_sign(biz_content)
# body['sign'] = sign
# body['biz_content'] = biz_content
# data['body'] = body
# print(data)

# biz_content = json.dumps({"merchant_id": "900029000000354"})  # 要进行加密的数据
# sign = rsa_sign(biz_content)
# print(sign)
# data = {"sign": sign, "charset": "UTF-8", "biz_content": biz_content,
#         "partner": "900029000000354", "sign_type": "RSA", "service": "trade.acc.balance"}
# print(type(data),type(biz_content))
# res = requests.post("https://test_nucc.bhecard.com:9088/api_gateway.do", data)
# print(res.text)




# test_data = ReadExcel("./../database/DemoAPITestCase.xlsx").read_data()
# # biz_content_read= ''
# # sign_read = ''
# print(test_data)
# body = ''
# for i in test_data:
#     print(type(i),i)
#     biz_content_read = eval(i['body'])['biz_content']
#     body = eval(i['body'])
#     biz_content = json.dumps(biz_content_read)
#     sign = rsa_sign(biz_content)
#     print(sign)
#     body['sign'] = sign
#     body['biz_content'] = biz_content
#     res = requests.post("https://test_nucc.bhecard.com:9088/api_gateway.do", body)
#     print(res.text)




















