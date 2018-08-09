#-*- coding:utf-8 -*-

######################################
#   开启访客WiFi，检查系统信息详情   #
#    前置条件：访客WiFi关闭状态      #
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
from modules.wifi import *
#创建测试对象
login = login_router()
router_s = router_setup()
config = configparser.ConfigParser()
wifi = wifi()

#获取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_pw")
guest_ssid = config.get("Default","default_guest")
url = r"http://" + web_ip
#创建测试方法
def check_open_guest_wifi_systeminfo(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,1) == 1:
                wifi.clickWiFi(driver,3)
                if router_s.setup_choose(driver,5) == 5:
                    return router_s.open_guest_wifi_systeminfo(driver,guest_ssid)


#创建测试用例
class Test_open_guest_wifi_systeminfo:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_open_guest_wifi_systeminfo(self):
        assert check_open_guest_wifi_systeminfo(self.driver) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))