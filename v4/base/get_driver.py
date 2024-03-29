from selenium import webdriver
from v4 import page


class GetDriver:
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.login_url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None