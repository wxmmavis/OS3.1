# -*- coding: utf-8 -*-

import configparser
import logging
import os
import time
import pytest
#import conftest
#########################
#  import module
#########################
import sys
sys.path.append("..")

from modules.login_router import *
from modules.initialize_new import *
from tools import *
#########################
from selenium import webdriver

lr = login_router()
setup = initialize()
t = tools()
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
config_file = projectpath + '/configure/' + 'testconfig.ini'
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip = config.get('Default', 'default_ip')
default_pw = config.get('Default', 'default_pw')
ssid_Illegal_long_number = config.get('SSID', 'ssid_Illegal_long_number')
ssid_Illegal_char = config.get("SSID","ssid_Illegal_char")
ssid_Illegal_long_chinese = config.get("SSID","ssid_Illegal_long_chinese")
logging.info(__file__)


def set_ssid_Illegal_char(driver):
    return setup.set_Illegal_ssid(driver, ssid_Illegal_char,default_pw)

def set_ssid_Illegal_long_number(driver):
    return setup.set_Illegal_ssid(driver, ssid_Illegal_long_number,default_pw)

def set_ssid_Illegal_long_chinese(driver):
    return setup.set_Illegal_ssid(driver, ssid_Illegal_long_chinese,default_pw)

class Test_Initialize_SSID:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if lr.open_url(self.driver, 'http://' + default_ip) == 2:
            if setup.homepageD1(self.driver) == 1:
                pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()
    #测试异常字符的SSID
    def test_set_ssid_Illegal_char(self):
        assert set_ssid_Illegal_char(self.driver) == 1
    #测试超长的数字SSID
    def test_set_ssid_Illegal_long_number(self):
        assert set_ssid_Illegal_long_number(self.driver) == 2
    #测试超长的中文字符SSID
    def test_set_ssid_Illegal_long_chinese(self):
        assert set_ssid_Illegal_long_chinese(self.driver) == 2



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
