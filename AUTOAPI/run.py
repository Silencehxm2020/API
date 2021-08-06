from unittestreport import TestRunner
import unittest


from 接口项目.tools.do_exl import DOEXL
from 接口项目.tools.get_filepath import GetFilePath
from 接口项目.tools.http_request import Http_request
from 接口项目.tools.read_config import ReadConfig
class RunTestcase:
    baseurl = ReadConfig.base_url
    @staticmethod
    def run():
        my_suite = unittest.defaultTestLoader.discover(r"G:\pythonProject\接口项目\test_case", "test_loging.py")
        runner = TestRunner(my_suite, report_dir="G:\pythonProject\接口项目\output\html_report", templates=1)
        runner.run()

RunTestcase.run()