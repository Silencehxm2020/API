from unittestreport import TestRunner
import unittest


from AUTOAPI.tools.do_exl import DOEXL
from AUTOAPI.tools.get_filepath import GetFilePath
from AUTOAPI.tools.http_request import Http_request
from AUTOAPI.tools.read_config import ReadConfig
class RunTestcase:
    baseurl = ReadConfig.base_url
    @staticmethod
    def run():
        my_suite = unittest.defaultTestLoader.discover(r"G:\pythonProject\AUTOAPI\test_case", "test_loging.py")
        runner = TestRunner(my_suite, report_dir="G:\pythonProject\AUTOAPI\output\html_report", templates=1)
        runner.run()

RunTestcase.run()