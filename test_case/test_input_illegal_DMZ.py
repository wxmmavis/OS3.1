#-*- coding:utf-8 -*-

############################
#   输入异常的DMZ IP地址   #
############################

import sys
import os
import pytest
import time
import configparser
from selenium import webdriver

#import测试库
sys.path.append("..")
from modules.login_router import *
from modules.advanced_setup import *

#创建测试对象
login = login_router()
advanced_setup = advanced_setup()
config = configparser.ConfigParser()

#读取配置文件
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_pw")
dmz_null = config.get("DMZ","null_dmz")
dmz_illegal = config.get("DMZ","illegal_dmz")
list = dmz_illegal.split()
url = r"http://" + web_ip

#创建测试方法
def check_illegal_DMZ(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                if advanced_setup.input_illegal_DMZ_ip(driver) == 1:
                    return advanced_setup.input_illegal_DMZ_ip(driver,list)



class Test_check_illegal_DMZ:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_illegal_DMZ(self):
        assert check_illegal_DMZ(self.driver) == 1


if __name__ == "__main__":
    pytest.main(os.path.basename(__file__))