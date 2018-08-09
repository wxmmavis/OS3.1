#-*- coding:utf-8 -*-

#############################################################
#   自动设置dns及手动dns不做设置，直接点击保存，检查提示语  #
#############################################################

import sys
import os
import time
import pytest
import configparser
from selenium import webdriver

#import测试库
sys.path.append("..")
from modules.login_router import *
from modules.router_setup import *

#创建测试对象
login = login_router()
router_s = router_setup()
config = configparser.ConfigParser()

#获取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_pw")
url = r"http://" + web_ip

#创建测试方法
def check_DHCP_set_nothong_dns(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                return router_s.get_nothing_set_message(driver)

#创建测试用例
class Test_DHCP_set_nothing_msg:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_check_DHCP_set_nothong_dns(self):
        assert check_DHCP_set_nothong_dns(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))



