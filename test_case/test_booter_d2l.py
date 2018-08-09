#-*- coding:utf-8 -*-

#########################
#   联想固件页脚检查    #
#########################

import sys
import os
import time
import pytest
import configparser
from selenium import webdriver

#import测试库函数
sys.path.append("..")
from modules.login_router import *

#创建对象
login = login_router()
config = configparser.ConfigParser()

#读取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
Official_network_url = config.get("d2l_booter_url","Official_network_url")
weibo_url = config.get("d2l_booter_url","weibo_url")
service_url = config.get("d2l_booter_url","service_url")
weixin_url = config.get("d2l_booter_url","weixin_url")
web_ip = config.get("Default","default_ip")
url = r"http://" + web_ip

#创建测试方法

#创建检查官方网站的方法
def check_Official_network_url(driver):
    if login.open_url(driver,url) == 1:
        return login.Official_network_url_d2l(driver,Official_network_url)
#创建检查官方微博的方法
def check_weibo_url(driver):
    if login.open_url(driver,url) == 1:
        return login.weibo_url_d2l(driver,weibo_url)
#创建检查服务网址的方法
def check_service_url(driver):
    if login.open_url(driver,url) == 1:
        return login.service_url_d2l(driver,service_url)
#创建检查官方微信的方法
def check_weixin_url(driver):
    if login.open_url(driver,url) == 1:
        return login.weixin_url_d2l(driver,weixin_url)

#创建测试用例
class Test_booter_d2l:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    #测试用例
    def test_check_Official_network_url(self):
        assert check_Official_network_url(self.driver) == 1
    def test_check_weibo_url(self):
        assert check_weibo_url(self.driver) == 1
    def test_check_service_url(self):
        assert check_service_url(self.driver) == 1
    def test_check_weixin_ur(self):
        assert check_weixin_url(self.driver) == 1

if __name__ == "__main__":
    pytest.main(os.path.basename(__file__))

