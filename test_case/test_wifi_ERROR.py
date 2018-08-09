# -*- coding: utf-8 -*-
import configparser
import logging
import time
import os
import pytest
#########################
#  import module
#########################
import sys
import conftest
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.wifi import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
t = tools()
w = wifi()
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
logging.info(__file__)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
default_24ssid = config.get('Default', 'default_ssid')
default_5ssid = default_24ssid + '_5G'
default_guest = config.get('Default', 'default_guest')
default_guestpw = config.get('Default', 'default_guestpw')
SSID24 = config.get('WiFi', 'ssid24')
SSID5 = config.get('WiFi', 'ssid5')
SSIDg = config.get('WiFi', 'ssidg')
pw24 = config.get('WiFi', 'pw24')
pw5 = config.get('WiFi', 'pw5')
pwg = config.get('WiFi', 'pwg')


def save_nochange(driver):
    if w.save_fail(driver)==1:
        return 1
    driver.get_screenshot_as_file(caseFail + "save_nochange-%s.jpg" % test_time)
    logging.warning('============================Fail')

####设置中文密码###
def  set_Chinese_PW(driver):
    if w.ChinesePW(driver)==1:
        return 1

########设置逗号密码#####
def set_commaPW(driver):
    if w.commaPW(driver)==1:
        return 1

########输入超过规定的字符数名称#######
def set_ERRORssid(driver):
    if w.setErrorSSID(driver)==1:
        return 1


class Test_WiFi:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 1) == 1:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    #######不修改任何内容点击保存#########
    def test_save_fail(self):
        assert save_nochange(self.driver) == 1

    ######输入中文密码######
    def test_input_Chinese_PW(self):
        assert set_Chinese_PW(self.driver)==1

    ######输入逗号密码#####
    def test_commaPW(self):
        assert set_commaPW(self.driver)==1

    #######输入超过规定的字符数名称#######
    def test_setERROR_ssid(self):
        assert set_ERRORssid(self.driver)==1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))