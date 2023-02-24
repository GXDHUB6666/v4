import time

from v4.base.base import Base
from v4 import page
from v4.tool.yaml_data import Yaml_until

class PageLogin(Base):
    # 点击登录链接
    def page_login_click(self):
        self.base_click(page.login_link)
    # 输入用户名
    def page_login_username(self,username):
        self.base_input(page.login_username,username)
    # 输入密码
    def page_login_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)
    # 输入验证码
    def page_login_code(self):
        pass
    # 点击登录按钮
    def page_login_click_btn(self):
        self.base_click(page.login_btn)
    def page_login_quit(self):
        self.base_click(page.login_quit)
    # 获取异常信息
    def page_get_err_info(self):
        return self.base_get_text(page.login_err_btn)
    # 点击信息框确定
    #def page_click_err_btn_ok(self):
       # self.base
    # 截图
    def page_get_screenshot(self):
        self.base_get_png()
    # 读取yaml
    def page_read_yml(self):
        return Yaml_until().yaml_read(page.login_data)
    # 组装
    def page_login(self,username,pwd):
        self.page_login_click()
        self.page_login_username(username)
        self.page_login_pwd(pwd)
        self.page_login_click_btn()
        self.page_get_err_info()

