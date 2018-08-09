#-*- coding:utf-8 -*-

################################
#   输入异常的静态IP地址检查   #
################################

import sys
import os
import time
import pytest
import configparser
from selenium import webdriver

#import测试库函数
sys.path.append("..")
from modules.router_setup import *
from modules.login_router import *
#创建测试对象
config = configparser.ConfigParser()
login = login_router()
router_s = router_setup()
#获取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding='UTF-8')
web_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_pw")
url = r"http://" + web_ip
static_ip_null = config.get("Static","ipaddr_illegal_null")
static_mask_null = config.get("Static","netmask_illegal_null")
static_gateway_null = config.get("Static","gateway_illegal_null")
dns1_null = config.get("Static","dns_null_01")
dns2_illegal = config.get("Static","dns_illegal_02")
static_ip_illegal = config.get("Static","gateway_illegal")
static_ip = config.get("Static","ipaddr")
static_mask_illegal = config.get("Static","netmask_illegal")
static_mask = config.get("Static","netmask")
static_gateway_illegal = config.get("Static","gateway_illegal")
static_gateway = config.get("Static","gateway")
dns_illegal_01 = config.get("Static","dns_illegal_01")
static_dns1 = config.get("Static","dns1")

#IP地址输入为空时，检查异常提示语
def check_input_null_ipaddress(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip_null,static_mask_null,static_gateway_null,dns1_null,dns2_illegal)

#ip地址输入异常时，检查提示语
def check_input_illegal_ipaddress(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip_illegal,static_mask_null,static_gateway_null,dns1_null,dns2_illegal)
#子网掩码输入为空时，检查提示语
def check_input_null_netmask(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip,static_mask_null,static_gateway_null,dns1_null,dns2_illegal)
#子网掩码输入异常时，检查提示语
def check_input_illegal_netmask(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip,static_mask_illegal,static_gateway_null,dns1_null,dns2_illegal)
#网关输入为空时，检查提示语
def check_input_null_gateway(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip,static_mask,static_gateway_null,dns1_null,dns2_illegal)
#网关输入异常时，检查提示语
def check_input_illegal_gateway(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip,static_mask,static_gateway_illegal,dns1_null,dns2_illegal)
#dns1输入为空时，检查提示语
def check_input_null_dns1(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip,static_mask,static_gateway,dns1_null,dns2_illegal)

#dns1输入异常时，检查提示语
def check_input_illegal_dns1(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip,static_mask,static_gateway,dns_illegal_01,dns2_illegal)

#dns2输入异常时，检查提示语
def check_input_illegal_dns2(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                 return router_s.get_static_illegal_msg(driver,static_ip,static_mask,static_gateway,static_dns1,dns2_illegal)

#创建测试用例
class Test_static_illegal_input:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_input_null_ipaddress(self):
        assert check_input_null_ipaddress(self.driver) == 1
    def test_check_input_illegal_ipaddress(self):
        assert check_input_illegal_ipaddress(self.driver) == 2
    def test_check_input_null_netmask(self):
        assert check_input_null_netmask(self.driver) == 3
    def test_check_input_illegal_netmask(self):
        assert check_input_illegal_netmask(self.driver) == 4
    def test_check_input_null_gateway(self):
        assert check_input_null_gateway(self.driver) == 5
    def test_check_input_illegal_gateway(self):
        assert check_input_illegal_gateway(self.driver) == 6
    def test_check_input_null_dns1(self):
        assert check_input_null_dns1(self.driver) == 7
    def test_check_input_illegal_dns1(self):
        assert check_input_illegal_dns1(self.driver) == 8
    def test_check_input_illegal_dns2(self):
        assert check_input_illegal_dns2(self.driver) ==9
if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))