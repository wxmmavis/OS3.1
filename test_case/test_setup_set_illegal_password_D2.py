#-*- coding:utf-8 -*-

##########################
#   初始化向导异常密码   #
##########################

import sys
import configparser
import os
from selenium import webdriver
import pytest

sys.path.append("..")
from modules.login_router import *
from modules.initialize_new import *

path = os.path.dirname(os.getcwd())
config = configparser.ConfigParser()
config.read(path+r"\configure\testconfig.ini",encoding="utf-8")
Illegal_short_pwd = config.get("Password","Illegal_short_pwd")
Illegal_long_pwd = config.get("Password","Illegal_long_pwd")
Illegal_char_pwd = config.get("Password","Illegal_char_pwd")
url_Default = config.get("Default","default_ip")
url = r"http://" + url_Default
#创建对象
login = login_router()
initialize = initialize()

#输入短的非法初始化密码
def input_Illegal_short_pwd(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.set_Illegal_password(driver,Illegal_short_pwd)

#输入长的非法初始化密码
def input_Illegal_long_pwd(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.set_Illegal_password(driver,Illegal_long_pwd)

#输出非法的特殊字符初始化面
def input_Illegal_char_pwd(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            return initialize.set_Illegal_password(driver,Illegal_char_pwd)


#执行用例
class Test_initialize_password:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
    #测试输入非法的初始化字符密码
    def test_input_input_Illegal_char_pwd(self):
        assert input_Illegal_char_pwd(self.driver) == 1
    #测试输入非法的过短初始化密码
    def test_input_Illegal_short_pwd(self):
        assert input_Illegal_short_pwd(self.driver) == 2
    #测试输入非法的过长初始化密码
    def test_input_input_Illegal_long_pwd(self):
        assert input_Illegal_long_pwd(self.driver) == 2


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))