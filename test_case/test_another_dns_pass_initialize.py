#-*- coding:utf-8 -*-

##################################################
#   使用其他的域名访问初始化页面并通过设置向导   #
##################################################

import sys
import os
import pytest
import logging
import configparser
import time
from selenium import webdriver
#import测试库函数

sys.path.append("..")

from modules.login_router import *
from modules.initialize_new import *

#创建对象
config = configparser.ConfigParser()
login = login_router()
initialize = initialize()

#获取文件路径
path = os.path.dirname(os.getcwd())

#读取配置文件
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
password = config.get("Default","default_pw")
url_ok_go = config.get("newifi_web_dns","url_ok_go")
url_wi_fi = config.get("newifi_web_dns","url_wi_fi")
url_xyun_co = config.get("newifi_web_dns","url_xyun_co")
url_newifi_com = config.get("newifi_web_dns","url_newifi_com")
#创建测试方法
def okgo_pass_initialize(driver):
    if login.open_url(driver,url_ok_go) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.close_initialize(driver,password)

def wifi_pass_initialize(driver):
    if login.open_url(driver,url_wi_fi) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.close_initialize(driver,password)

def xyunco_pass_initialize(driver):
    if login.open_url(driver,url_xyun_co) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.close_initialize(driver,password)

def newificom_pass_initialize(driver):
    if login.open_url(driver,url_newifi_com) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.close_initialize(driver,password)

#创建测试用例
class Test_another_dns_initialize:
    def setup(self):
        self.driver = webdriver.Chrome()
    def teardown(self):
        self.driver.quit()

    #输入ok.go进入初始化页面，并通过设置向导
    def test_okgo_pass_initialize(self):
        assert okgo_pass_initialize(self.driver) == 1
     #输入wi.fi进入初始化页面，并通过设置向导
    def test_wifi_pass_initialize(self):
        assert wifi_pass_initialize(self.driver) == 1
     #输入xyun.co进入初始化页面，并通过设置向导
    def test_xyunco_pass_initialize(self):
        assert xyunco_pass_initialize(self.driver) == 1
     #输入newifi.com进入初始化页面，并通过设置向导
    def test_newificom_pass_initialize(self):
        assert newificom_pass_initialize(self.driver) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))