#-*- coding:utf-8 -*-

######################################
#           关闭系统信息弹框         #
######################################

import sys
import os
import time
import pytest
import configparser
from selenium import webdriver

#import测试库函数
sys.path.append("..")
from modules.login_router import *
from modules.router_setup import *
#创建测试对象
login = login_router()
router_s = router_setup()
config = configparser.ConfigParser()

#获取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_pw")
guest_ssid = config.get("Default","default_guest")
url = r"http://" + web_ip
#创建测试方法
def check_close_systeminfo(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.close_systeminfo(driver)


#创建测试用例
class Test_close_systeminfo:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_close_systeminfo(self):
        assert check_close_systeminfo(self.driver) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))