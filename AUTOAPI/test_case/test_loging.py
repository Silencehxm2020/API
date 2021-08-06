import unittest
import ddt
from 接口项目.run import RunTestcase
from 接口项目.test_data.before_testdta import Beforedata
from 接口项目.tools.do_exl import DOEXL
from 接口项目.tools.get_filepath import GetFilePath
from 接口项目.tools.http_request import Http_request

import json

data = Beforedata.do_test_data('test_data', 'test_da.xlsx', 'login')
filepath = GetFilePath.file_path('test_data', 'test_da.xlsx')


@ddt.ddt()
class Test_Login(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ddt.data(*data)
    def test_login(self, item):
        # print(item)
        result = Http_request(RunTestcase.baseurl + item["URL"], item["请求方式"], eval(item['参数'])).do_request()
        expect_code = eval(DOEXL.do_null_and_true(item["期望结果"]))["code"]
        # print(type(item["序号"]))
        self.assertEqual(expect_code, result["code"])
        try:
            DOEXL(filepath, "login").write_back(item["序号"] + 1, 8, str(result))
        except Exception as e:
            print("表格写入失败：{}".format(e))
            raise e
        finally:
            if expect_code == result["code"]:
                DOEXL(filepath, "login").write_back(item["序号"] + 1, 9, "pass")
            else:
                DOEXL(filepath, "login").write_back(item["序号"] + 1, 9, "fail")
