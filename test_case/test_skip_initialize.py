#-*- coding:utf-8 -*-

###################################
#   跳过设置向导直接打开完成页面  #
###################################

import pytest
from selenium import webdriver
import sys
import configparser
import os

sys.path.append("..")
from modules.login_router import *

path = os.path.dirname(os.getcwd())
login = login_router()
config = configparser.ConfigParser()

config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
url = web_ip + r"/finish.html"

def skip_initialize(driver):
    return login.open_url(driver,url)

#http://192.168.99.1/finish.html
class Test_skip_initialize:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_skip_initialize(self):
        assert skip_initialize(self.driver) == 0

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))