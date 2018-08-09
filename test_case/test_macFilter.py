# -*- coding: utf-8 -*-

import time
import sys
import os
import pytest
import configparser
from selenium import webdriver


#import测试库函数
sys.path.append("..")
from modules.login_router import *
from modules.advanced_setup import *

#创建测试对象
login = login_router()
advanced_setup = advanced_setup()
config = configparser.ConfigParser()

#读取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
url = r"http://" + web_ip
pwd = config.get("Default","default_pw")
mac_name_list = config.get("macfilter","mac_name").split()
mac_addr_list = config.get("macfilter","mac_address").split()


#创建测试方法
#检查mac过滤的默认状态
def check_defualt_macfilter_status(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.check_macfilter_status(driver)
#检查mac过滤页面内容
def check_macfilter_web(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.check_macfilter_web(driver)
#输入为空的mac过滤名称
def check_null_macfilter_name(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.Manual_addition_macFilter(driver)
#输入异常的MAC地址
def check_abnomal_macfilter_mac(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                name = ["test"]
                return advanced_setup.Manual_addition_macFilter(driver,name,mac_addr_list)

#输入空的MAC地址
def check_null_macfilter_mac(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                name = ["test"]
                return advanced_setup.Manual_addition_macFilter(driver,name)

#保存一个MAC过滤地址，并删除
def check_save_and_delete_macfilter(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                name = "test"
                mac = "00:1d:0f:11:22:33"
                return advanced_setup.save_and_delete_macfilter(driver,name,mac)
#创建测试用例
class Test_check_defualt_macfilter_status:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_defualt_macfilter_status(self):
        assert check_defualt_macfilter_status(self.driver) == 1

    def test_check_macfilter_web(self):
        assert check_macfilter_web(self.driver) == 1

    def test_check_null_macfilter_name(self):
        assert check_null_macfilter_name(self.driver) == 1

    def test_check_abnomal_macfilter_mac(self):
        assert check_abnomal_macfilter_mac(self.driver) == 4

    def test_check_null_macfilter_mac(self):
        assert check_null_macfilter_mac(self.driver) == 3

    def test_check_save_and_delete_macfilter(self):
        assert check_save_and_delete_macfilter(self.driver) == 1



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))

