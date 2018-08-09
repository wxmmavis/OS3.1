#-*- coding:utf-8 -*-
#####################################
#   检查初始化向导默认的SSID名称    #
#####################################

from selenium import webdriver
import sys
import os
import configparser
import pytest

#import测试函数
sys.path.append("..")
from modules.login_router import *
from modules.initialize_new import *

#创建对象
login = login_router()
initialize = initialize()
config = configparser.ConfigParser()

#读取配置文件
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding = "utf-8")
web_ip = config.get("Default","default_ip")
default_ssid = config.get("Default","default_ssid")
url = r"http://" + web_ip

#创建测试方法
def check_default_ssid_initialize(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            if initialize.get_default_ssid(driver) == default_ssid:
                return 1


#创建测试用例
class Test_default_ssid_initialize:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    #测试用例
    def test_check_default_ssid_initialize(self):
        assert check_default_ssid_initialize(self.driver) == 1

if __name__ == "__main__":
    pytest.main(os.path.basename(__file__))