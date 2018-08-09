#-*- coding:utf-8 -*-

##############################
#   输入异常的mac克隆地址    #
##############################

import sys
import os
import pytest
import time
import configparser
from selenium import webdriver

#import 测试函数
sys.path.append("..")
from modules.login_router import *
from modules.router_setup import *

#创建对象
login = login_router()
r_setup = router_setup()
config = configparser.ConfigParser()

#读取配置文件
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
illegal_mac = config.get("Mac","illegal_mac")
illegalchar_mac = config.get("Mac","illegalchar_mac")
illegal_man_null = config.get("Mac","illegal_mac_null")
web_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_pw")

url = r"http://" + web_ip


#创建测试方法
#检查异常的mac克隆地址
def check_illegal_mac(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if r_setup.setup_choose(driver,2) == 2:
                return r_setup.set_illegal_macclone(driver,illegal_mac)
#检查异常字符的mac克隆地址
def check_illegalchar_mac(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if r_setup.setup_choose(driver,2) == 2:
                return r_setup.set_illegal_macclone(driver,illegalchar_mac)
#检查空的mac克隆地址
def check_illegal_mac_null(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if r_setup.setup_choose(driver,2) == 2:
                return r_setup.set_illegal_macclone(driver,illegal_man_null)


class Test_illegal_macclone:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
#测试异常的mac克隆地址
    def test_check_illegal_mac(self):
        assert check_illegal_mac(self.driver) == 1
#测试异常字符的mac克隆地址
    def test_check_illegalchar_mac(self):
        assert check_illegalchar_mac(self.driver) == 1
#测试空的mac克隆地址
    def test_check_illegal_mac_null(self):
        assert check_illegal_mac_null(self.driver) == 2

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))