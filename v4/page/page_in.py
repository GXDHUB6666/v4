from HM头条.base.base import Base
from HM头条.page.page_hmtt import PageLogin


class PageIn:

    def __init__(self,driver):
        self.driver=driver

    # 获取pagelogin对象
    def page_get_pagelogin(self):
        return PageLogin(self.driver)
    #