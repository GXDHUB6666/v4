import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from v4.tool.get_log import get_logging
log = get_logging()

class Base:

    # 初始化
    def __init__(self,driver):
        self.driver = driver


    # 查找元素方法
    def base_find_element(self,loc,timeout=10):
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=0.5).until(lambda x:x.find_element(*loc)) # *loc对此元组进行解包
    # 点击方法
    def base_click(self,loc):
        log.info("正在点击元素：{}".format(loc))
        self.base_find_element(loc).click()
    # 输入方法
    def base_input(self,loc,value):
        log.info("正在给元素{} 输入内容：{}".format(loc,value))
        el = self.base_find_element(loc)
        el.clear()
        log.info("正在清空元素：{}".format(loc))
        el.send_keys(value)
        log.info("正在给元素{} 输入内容：{}".format(loc,value))
    # 获取文本方法
    def base_get_text(self,loc):
        log.info("获取元素文本：{}".format(loc))
        return self.base_find_element(loc).text
    # 截图方法
    def base_get_png(self):
        log.info("正在截图")
        self.driver.get_screenshot_as_file(f'../image/{time.strftime("%Y-%m-%d-%H-%M-%S")}.png')
