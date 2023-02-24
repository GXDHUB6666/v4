import time
import unittest

from parameterized import parameterized
from v4.base.get_driver import GetDriver
from v4.page.page_login import PageLogin
from v4.tool.yaml_data import Yaml_until
from v4.tool.get_log import get_logging
log = get_logging()

class TestLogin(unittest.TestCase):
    login = None

    @classmethod
    def setUpClass(cls):
        # 实例化 获取页面对象
        try:
            driver = GetDriver().get_driver()
            cls.login = PageLogin(driver)
        # 点击登录链接
        except Exception as e:
            log.error(e)

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()


    @parameterized.expand(Yaml_until().data())
    def test_login(self,username,pwd,expect,success):
        self.login.page_login(username,pwd)
        msg = self.login.page_get_err_info()
        print(msg,expect)
        if success:
            try:
                assert msg == expect
                self.login.page_login_quit()
            except Exception as e:
                log.error(e)
                self.login.page_get_screenshot()
        else:
            try:
                self.assertEqual(msg,expect)
            except AssertionError as e:
                log.error(e)
                self.login.page_get_screenshot()

