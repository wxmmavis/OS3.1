#-*- coding:utf-8 -*-

##################################
#   高级设置修改密码栏异常测试   #
##################################

import sys
import os
import pytest
import time
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
wifi = wifi()
config = configparser.ConfigParser()

#获取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
login_password = config.get("Default","default_pw")
ssid_24G = config.get("WiFi","ssid24")
ssid_5G = config.get("WiFi","ssid5")
channel_24G = config.get("WiFi","ht_24")
channel_5G = config.get("WiFi","ht_5")
url = r"http://" + web_ip
#创建测试方法

def modify_ssid_htMode_systeminf(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,1) == 1:
                wifi.setSSID(driver,1,ssid_24G)
                wifi.advance(driver,1)
                wifi.setChannel_new(driver,1,5)
                wifi.savewifi(driver,1)
                time.sleep(10)
                wifi.setSSID(driver,2,ssid_5G)
                wifi.advance(driver,2)
                wifi.setChannel_new(driver,2,149)
                wifi.savewifi(driver,2)
                time.sleep(10)
                if router_s.setup_choose(driver,5) == 5:
                    return router_s.modify_ssid_htMode_systeminfo(driver,ssid_24G,ssid_5G,channel_24G,channel_5G)


#创建测试用例
class Test_modify_systeminfo:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_modify_ssid_htMode_systeminf(self):
        assert modify_ssid_htMode_systeminf(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
