#-*- coding:utf-8 -*-

##############################
#   初始化页面返回按钮功能   #
##############################

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
pppoe_ursname = config.get("PPPOE","PPPOE_username")
pppoe_password = config.get("PPPOE","PPPOE_password")
url = r"http://" + web_ip

#DHCP环境下返回上一页
def DHCP_comeback_initialize(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            if initialize.PPPOE_DHCP_comeback_initialize(driver) == 1:
                return initialize.homepageD1(driver)
#PPPOE环境下返回上一页

def PPPOE_comeback_initialize(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            if initialize.input_pppoe_username_password_initialize(driver,pppoe_ursname,pppoe_password) == 1:
                if initialize.PPPOE_DHCP_comeback_initialize(driver) == 1:
                    if initialize.PPPOE_DHCP_comeback_initialize(driver) == 1:
                        return initialize.homepageD1(driver)

class Test_PPPOE_DHCP_comeback_initialize:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    #测试DHCP环境下返回上一页
    def test_DHCP_comeback_initialize(self):
        assert DHCP_comeback_initialize(self.driver) == 1

    #测试PPPOE环境下返回上一页
    #def test_PPPOE_comeback_initialize(self):
        #assert PPPOE_comeback_initialize(self.driver) == 1
if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))