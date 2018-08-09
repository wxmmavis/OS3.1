#-*- coding:utf-8 -*-

##################################################
#   手动设置dns时，不填写dns直接点击保存按钮     #
##################################################

import sys
import os
import pytest
import configparser
import time
from selenium import webdriver

#import测试库函数
sys.path.append("..")
from modules.login_router import *
from modules.router_setup import *

#创建测试对象
config = configparser.ConfigParser()
login = login_router()
router_set  = router_setup()
#获取配置文件
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
url = r"http://" + web_ip
pwd = config.get("Default","default_pw")
dns_null_01 = config.get("Static","dns_null_01")
dns_null_02 = config.get("Static","dns_null_02")
dns_illegal_01 = config.get("Static","dns_illegal_01")
dns_illegal_02 = config.get("Static","dns_illegal_02")
dns_right = config.get("Static","dns1")
#创建测试方法
#两个输入框都不输入任何值
def check_set_all_nothing(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_set.setup_choose(driver,2) == 2:
                return router_set.set_DHCP_null_dns(driver)
#两个输入框输入空值
def check_set_all_null(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_set.setup_choose(driver,2) == 2:
                return router_set.set_DHCP_illegal_dns(driver,dns_null_01,dns_null_02)

#第一个dns输入框输入异常的dns
def check_set_dns01_illegal(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_set.setup_choose(driver,2) == 2:
                return router_set.set_DHCP_illegal_dns(driver,dns_illegal_01)
#第二个dns输入框输入异常的dns
def check_set_dns02_illegal(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_set.setup_choose(driver,2) == 2:
                return router_set.set_DHCP_illegal_dns(driver,dns_right,dns_illegal_02)



#创建测试用例

class Test_null_dns:
    def setup(self):
        self.diver = webdriver.Chrome()

    def teardown(self):
        self.diver.quit()

    def test_check_set_all_null(self):
        assert check_set_all_nothing(self.diver) == 1
    def test_check_set_all_null(self):
        assert check_set_all_null(self.diver) == 1
    def test_check_set_dns01_illegal(self):
        assert check_set_dns01_illegal(self.diver) == 2
    def test_check_set_dns02_illegal(self):
        assert check_set_dns02_illegal(self.diver) == 3

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))

