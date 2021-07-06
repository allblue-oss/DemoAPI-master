#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os,sys,json
import warnings

import urllib3
from nb_log import LogManager
from package.RSA_encrypt_sign import rsa_sign

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,requests,ddt
from config import setting
from lib.readexcel import ReadExcel
from lib.sendrequests import SendRequests
from lib.writeexcel import WriteExcel

testData = ReadExcel(setting.SOURCE_FILE, "Sheet1").read_data()
log_path = os.path.join(os.path.dirname(__file__),'../log')
logger = LogManager(__file__).get_logger_and_add_handlers(log_level_int=10,log_path=log_path,log_filename='log2021.log')
@ddt.ddt
class Demo_API(unittest.TestCase):
    """XX项目接口测试"""
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s = requests.session()

    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self,data):

        #获取测试用例名称
        self._testMethodDoc = data['UseCase']

        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[2])
        logger.info("******* 正在执行用例 ->{0} *********".format(data['ID']))
        logger.info("请求方式: {0}，请求URL: {1}".format(data['method'],data['url']))
        logger.info("请求参数: {0}".format(data['params']))
        logger.info("post请求body类型为：{0} ,body内容为：{1}".format(data['type'], data['body']))


        # RSA加签
        body = eval(data['body'])
        biz_content_read = eval(data['body'])['biz_content']
        biz_content = json.dumps(biz_content_read)
        sign = rsa_sign(biz_content)
        body['sign'] = sign
        body['biz_content'] = biz_content
        data['body'] = body


        # 发送请求
        urllib3.disable_warnings()
        re = SendRequests().sendRequests(self.s,data)
        # 获取服务端返回的值
        self.result = re.json()
        logger.info("接口返回信息：%s" % re.content.decode("utf-8"))
        # 获取excel表格数据的状态码和消息
        readData_code = data["resultcode"]
        readData_msg = data["msg"]
        if readData_code == self.result['trade_acc_balance_response']['code'] and readData_msg == self.result['trade_acc_balance_response']['msg']:
            OK_data = "PASS"
            logger.info("用例测试结果:  {0}---->{1}".format(data['ID'],OK_data))
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1,OK_data)
        if readData_code != self.result['trade_acc_balance_response']['code'] or readData_msg != self.result['trade_acc_balance_response']['msg']:
            NOT_data = "FAIL"
            logger.info("用例测试结果:  {0}---->{1}".format(data['ID'], NOT_data))
            WriteExcel(setting.TARGET_FILE).write_data(rowNum + 1,NOT_data)
        self.assertEqual(self.result['trade_acc_balance_response']['code'], readData_code, "返回实际结果是->:%s" % self.result['trade_acc_balance_response']['code'])
        self.assertEqual(self.result['trade_acc_balance_response']['msg'], readData_msg, "返回实际结果是->:%s" % self.result['trade_acc_balance_response']['msg'])

if __name__=='__main__':
    unittest.main()
