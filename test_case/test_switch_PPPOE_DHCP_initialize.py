#-*- coding:utf-8 -*-

################################
#   初始化页面PPPOE&DHCP转换   #
################################

import pytest
import sys
import os
import configparser
from selenium import webdriver

sys.path.append("..")
from modules.login_router import *
from modules.initialize_new import *

config = configparser.ConfigParser()
login = login_router()
initialize = initialize()
path = os.path.dirname(os.getcwd())

config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
url = r"http://" + web_ip

#DHCP跳转到PPPOE页面

def DHCP_switch_to_PPPOE(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.switch_PPPOE_DHCP_initialize(driver)
#PPPOE跳转到DHCP页面
def PPPOE_switch_to_DHCP(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            if initialize.switch_PPPOE_DHCP_initialize(driver)==1:
                return initialize.switch_PPPOE_DHCP_initialize(driver)

#测试用例
class Test_initialize_switch:
    def setup(self):
        self.driver = webdriver.Chrome()
    def teardown(self):
        self.driver.quit()
    #测试HCP跳转到PPPOE页面
    def test_DHCP_switch_to_PPPOE(self):
        assert DHCP_switch_to_PPPOE(self.driver) == 1
    #测试PPPOE跳转到DHCP页面
    def test_PPPOE_switch_to_DHCP(self):
        assert PPPOE_switch_to_DHCP(self.driver) == 2

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))