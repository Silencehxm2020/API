from unittestreport import TestRunner
import unittest



from tools.read_config import ReadConfig
class RunTestcase:
    baseurl = ReadConfig.base_url
    @staticmethod
    def run():
        my_suite = unittest.defaultTestLoader.discover(r"G:\pythonProject\AUTOAPI\test_case", "test_loging.py")
        runner = TestRunner(my_suite, report_dir="G:\pythonProject\AUTOAPI\output\html_report", templates=1)
        runner.run()

RunTestcase.run()