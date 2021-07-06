#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = '杜云慧'

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG =  os.path.join(BASE_DIR,"database","config.ini")
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR,"database","DemoAPITestCase.xlsx")
# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","DemoAPITestCase.xlsx")
# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR,"testcase")
# 网支测试环境KEY
TEST_ENVIRONMENT_KEY = 'MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBAIqUuxd92eEBXVneDWhfNP6XCkLcGBO1YAulexKX+OdlfZzB/4NNHkOAQQy84k3ZgIUPIk5hewLbA+XGrk9Wih5HG3ZQeFugeoTcx3vwo7AQv7KnmcKEWFNlOr/EhB3JndmcQnBRsIRRdCP+7nobfBqU0jS8dnpcQX1AtBRZRnkfAgMBAAECgYAe+u70ansZ1Q9EduKycY5MWAHAPqnXRhXppJ3l4zmOqV6ye6Aef1ADsRlZuqQw2S3lESQPN7WjRskRRiBTtjn8Atul9YeC7+QirP1K8seUP5gKB4bcjlzzl1m5dmxldkptJAmdzwYn8PRTW0+tFVyEaD/B8hKGxij4Gew0e8bwCQJBAOboG3ttBESsG2cAtmP1MfKRTjVdY7qRMXzBybcAeobBbmgCQgybVXXgjbGai+qwrQqcVRIp6p1yDWTZxVSuDWsCQQCZpBhcayOCMZR6F8dQJSuSSSIJw/GGN7IXfMYIqLxA2oGzlQ0B1DffOUe2wrid+WdpLuYCz2LYPQHDEgYM1dwdAkEAnfwhEYm9ad73wLnUEQAqdHTGtex316aP3XQZt4Q0UQ73o2IoHsgI6OYDDIlZQfIv8xqTeiIDzEXEtEPrp8yOkQJBAIWAzFZKFqHD2UO6M8vVcKX9fGFF7TH2ZX75Qc82Z9ZmyDs2sgW71QzX5hPN4cQLeqswQFeCw14orMZHfBBdKJUCQQDiWYk85okRugsWtxeJFhMEt2oUT+Kd8Yz5Aiz3J9XIS+zWtJrFlv+hXkVedPJ3xtBF32DZrCbxDn3UjXipRaCP'
# 网支生产环境KEY
NEY_PAY_KEY = 'MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBALLfMUbf4u8uDSeG0WR//LSvxv7qglKsHwws3mpyqUWJau1ZXcfMeNQf+OhGTFrKsyP1WS3kXa1ZErjIhdeX5Jq2TphgXWZ+HdNVtd/rmHo84cjHJZOOBSvSmVYzqsJT253LoX1ip2sx/zbobU+Sm//4I5Zo4/yuufWBElCL2cuPAgMBAAECgYEApkJ3Fx27Xf48E+VodDXSulA4c3GeuSFrqnF6Ow9g71WPohZS6QfRt7oQLjZJeoq2gFHpFpMRz7LfiAo6/e4deXEWtMRg4UHcZbdBlTR4oM8au1TTEq446VhllSNZ8qeHxL4zO4peVDNupp8rElOMTXiQLKOph+fioLi++tvqZGECQQDrvtI3QD68BEQXlwMcUHkczppTs3Gxtd5uElQ7BQCTpM1fBhFIzv+TNxhNLGo5+2z1MKjWNE1KBo1ZXZnJdSfLAkEAwj1ykXJkYWbNrTRGzh0ZjSg784c20TeEl2HZ4BvSdCwSRxZUdZYx4x6MUWISlnokaifXSJhnsU9vXoZR4xEKzQJBAN5SJdNfLgqIB2Mr0g4owh7tpFLdPpJ2Tl8FwBOswv96AwfjI/fC5vmBktRs13z45KdSjVb9Ggp+pVyqzfZUGwMCQGdPWWVEq2Em1ZQe7t3nmlR6ptBTBXPnjG0bzU8mXRwO6LXIial09hmvgMA0YmCInF+dyyJAdT5YWoqy9FDKGq0CQQCBstxGn3LUWcGxEmTtmDt3pkHVy2IYQl/xFCgWYW1xIrC7dO8GfLZLzUbq/yBGO1KCRaQpFYKbJNTETB0TlKSY'

