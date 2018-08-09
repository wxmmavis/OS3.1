# -*- coding: utf-8 -*-
import configparser
import logging
import os
import time
import csv
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
from modules.initialize import *
from modules.device_management import *
from modules.relay import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
rs = router_setup()
t = tools()
r = relay()
w=wifi()
projectpath = os.path.dirname(os.getcwd())
caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
logging.info(__file__)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
wds_pw = config.get('WDS', 'wds_pw')
ra0 = 1
rai0 = 2



def Check_Default_Relay_Status(driver):
    if r.relay(driver) == 1:
        logging.info("====================================Success")
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "defaultRelay-%s.jpg" % test_time)
        logging.warning("==================Fail")

def Open_Relay(driver):
    if r.clickRelay_D2(driver,"close") == 2:
        logging.info("====================================Success")
        return 2
    else:
        logging.info("====================================Fail")

def Cancel_24G_Conn_Relay(driver):
    if r.inputRelayPW(driver, wds_pw, ra0, 2) == 2:
        logging.info("====================================Success")
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "relayConnCancel-%s.jpg" % test_time)
        logging.warning("==================Fail")

def Sure_24G_Conn_Relay(driver):
    if r.inputRelayPW(driver, wds_pw, ra0, 1) == 1:
        logging.info("====================================Success")
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "relayConnSure-%s.jpg" % test_time)
        logging.warning("==================Fail")

def relay_errorPW(driver):
    if r.relay_errorPW(driver)==1:
        logging.info("===========================Success")
        return 1

def Close_Relay(driver):
    if r.clickRelay_D2(driver,"open") == 3:
        logging.info("====================================Success")
        return 2
    else:
        logging.info("====================================Fail")
def Close_Relay_restore(driver):
    if rs.setup_choose(driver,2)==2:
        if r.restore_DHCP(driver)==1:
            logging.info("====================================Success")
            return 1
        else:
            logging.info("====================================Fail")

def Reopen_Relay(driver):
    if r.clickRelay_D2(driver,"close") == 1:
        logging.info("====================================Success")
        return 1
    else:
        logging.info("====================================Fail")

def Cancel_Clear_24G_Relay(driver):
    if r.clearRelay(driver, ra0, 2) != 1:
        driver.get_screenshot_as_file(caseFail + "relayClearCancel-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
        logging.info('relayClearCancel === Fail')
    else:
        logging.info("====================================Success")
        return 1

def Sure_Clear_24G_Relay(driver):
    if r.clearRelay(driver, ra0, 1) != 2:
        driver.get_screenshot_as_file(caseFail + "relayClearSure-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
        logging.info('relayClearSure === Fail')
    else:
        logging.info("====================================Success")
        return 2

def Cancel_5G_Conn_Relay(driver):
    if r.inputRelayPW(driver, wds_pw, rai0, 2)==2:
        driver.get_screenshot_as_file(caseFail + "relay5GConnCancel-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
        logging.info('relay5GConnCancel === Fail')
    else:
        logging.info("====================================Success")
        return 2

def Sure_5G_Conn_Relay(driver):
    if r.inputRelayPW(driver, wds_pw, rai0, 1) == 1:
        logging.info("====================================Success")
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "relay5GConnSure-%s.jpg" % test_time)
        logging.warning("==================Fail")

def Sure_Clear_5G_Relay(driver):
    if r.clearRelay(driver, 2, 1) == 2:
        logging.info("====================================Success")
        return 2
    else:
        driver.get_screenshot_as_file(caseFail + "relay5GClearSure-%s.jpg" % test_time)
        logging.warning("==================Fail")

def relay_sameIP(driver):
    if r.relay_sameIP(driver)==1:
        logging.info("check success")
        return 1
    else:
        driver.get_screenshot_as_file(caseFail + "relaysameIP-%s.jpg" % test_time)
        logging.warning("==================Fail")

def Closed_Relay(driver):
    return r.clickRelay_D2(driver,"open")



class Test_Relays:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://'+default_ip) == 1:
            if lr.login(self.driver, default_pw) == 1:
                if rs.setup_choose(self.driver, 3) == 3:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_Check_Default_Relay_Status(self):
        print(u'检查无线中继默认状态')
        assert Check_Default_Relay_Status(self.driver) == 1

    def test_Open_Relay(self):
        print(u'打开无线中继')
        assert Open_Relay(self.driver) == 2

    def test_Cancel_24G_Conn_Relay(self):
        print(u'取消2.4G无线中继连接')
        assert Cancel_24G_Conn_Relay(self.driver) == 2

    def test_Sure_24G_Conn_Relay(self):
        print(u'确认2.4G无线中继连接')
        assert Sure_24G_Conn_Relay(self.driver) == 1



    def test_Close_Relay(self):
        print(u'关闭无线中继')
        assert Close_Relay(self.driver) == 2

    ####检查是否切换到dhcp#######
    def test_CloseToRestore(self):
        print("关闭中继自动切换DHCP")
        assert Close_Relay_restore(self.driver)==1

    def test_Reopen_Relay(self):
        print(u'重新打开无线中继')
        assert Reopen_Relay(self.driver) == 1

    def test_Cancel_Clear_24G_Relay(self):
        print(u'取消清除2.4G无线中继连接')
        assert Cancel_Clear_24G_Relay(self.driver) == 1

    def test_Sure_Clear_24G_Relay(self):
        print(u'确定清除2.4G无线中继连接')
        assert Sure_Clear_24G_Relay(self.driver) == 2
    #######中继输入错误密码###########
    def test_errorPW(self):
        assert relay_errorPW(self.driver) == 1

    def test_Cancel_5G_Conn_Relay(self):
        print(u'取消5G无线中继连接')
        assert Cancel_5G_Conn_Relay(self.driver) == 2

    def test_Sure_5G_Conn_Relay(self):
        print(u'确定5G无线中继连接')
        assert Sure_5G_Conn_Relay(self.driver) == 1

    def test_Sure_Clear_5G_Relay(self):
        print(u'确定5G清除无线中继连接')
        assert Sure_Clear_5G_Relay(self.driver) == 2

    ####中继相同IP WIFI######
    def test_relaySameIp(self):
        assert relay_sameIP(self.driver)==1

    def test_Closed_Relay(self):
        print(u'关闭无线中继')
        assert Closed_Relay(self.driver) == 3

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))