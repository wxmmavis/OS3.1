#-*- coding:utf-8 -*-

###############################
#   初始化向导PPPOE拨号测试   #
###############################
#import库函数
import sys
import time
import os
import pytest
import configparser
from selenium import webdriver

#imoprt 测试模块
sys.path.append("..")
from modules.login_router import *
from modules.initialize_new import *

#创建对象
login = login_router()
initialize = initialize()
config = configparser.ConfigParser()

#获取路径
path = os.path.dirname(os.getcwd())

#获取配置参数
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
pppoe_username = config.get("PPPOE","PPPOE_username")
pppoe_password = config.get("PPPOE","PPPOE_password")
pppoe_error_user = config.get("PPPOE","PPPOE_error_user")
pppoe_error_pwd = config.get("PPPOE","PPPOE_error_pwd")

url = r"http://" + web_ip

###创建测试方法
#pppoe模式下输入错误的PPPOE账号密码
def pppoe_input_error_usr_pwd(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            if initialize.switch_PPPOE_DHCP_initialize(driver) == 1:
                error = "not pass"
                return initialize.input_pppoe_username_password_initialize(driver,pppoe_error_user,pppoe_error_pwd,error)
#pppoe模式下输入正确的PPPOE账号密码
def pppoe_input_right_usr_pwd(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.input_pppoe_username_password_initialize(driver,pppoe_username,pppoe_password)


class Test_input_usr_pwd_pppoe:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    #测试pppoe模式下输入错误的PPPOE账号密码
    def test_pppoe_input_error_usr_pwd(self):
        assert pppoe_input_error_usr_pwd(self.driver) == 2
    # #测试pppoe模式下输入正确的PPPOE账号密码
    # def test_pppoe_input_right_usr_pwd(self):
    #     assert pppoe_input_right_usr_pwd(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))






