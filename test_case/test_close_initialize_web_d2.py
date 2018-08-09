#-*- coding:utf-8 -*-

###################################
#   初始化配置完成前关闭浏览器   #
##################################
#import库函数
import sys
import time
import os
import pytest
import configparser
from selenium import webdriver

#imoprt 测试模块
sys.path.append("..")
from modules.login_router import *
from modules.initialize_new import *

#创建对象
login = login_router()
initialize = initialize()
config = configparser.ConfigParser()

#获取路径
path = os.path.dirname(os.getcwd())

#获取配置参数
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
initialize_pwd = config.get("Default","default_pw")
pppoe_username = config.get("PPPOE","PPPOE_username")
pppoe_password = config.get("PPPOE","PPPOE_password")


url = r"http://" + web_ip
##创建测试方法
#DHCP模式下初始化完成前关闭网页再打开
def DHCP_befor_finish_initialize(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.close_initialize(driver,initialize_pwd)
def reopen_web(driver):
    return login.open_url(driver,url)

#PPPOE模式下初始化完成前关闭网页再打开
def PPPOE_befor_finish_initialize(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            if initialize.input_pppoe_username_password_initialize(driver,pppoe_username,pppoe_password) == 1:
                return initialize.close_initialize(driver,initialize_pwd)
def reopen_web(driver):
    return login.open_url(driver,url)

class Test_befor_finish_initialize:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        #login.open_url(self.driver,url)
        self.driver.quit()
    #测试DHCP模式下初始化完成前关闭网页
    def test_DHCP_befor_finish_initialize(self):
        assert DHCP_befor_finish_initialize(self.driver) == 1
    def test_reopen_web(self):
        assert reopen_web(self.driver) == 2
    #测试PPPOE环境下初始化完成前关闭网页
    # def test_PPPOE_befor_finish_initialize(self):
    #     assert PPPOE_befor_finish_initialize(self.driver) == 1
    # def test_reopen_web(self):
    #     assert reopen_web(self.driver) == 2


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))






