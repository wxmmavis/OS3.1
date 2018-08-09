#-*- coding:utf-8 -*-

###########################
#   测试点击忘记密码按钮  #
###########################

#import库函数
import sys
import os
import time
import pytest
import configparser
from selenium import  webdriver

#import测试modules
sys.path.append("..")
from modules.login_router import *
from modules.initialize_new import *

#创建测试对象
login = login_router()
initialize = initialize()
config = configparser.ConfigParser()

#获取文件路径
path = os.path.dirname(os.getcwd())

#读取配置文件
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
initialize_pwd = config.get("Default","default_pw")
url = r"http://" + web_ip

#创建测试方法

def click_forget_password(driver):
    if login.open_url(driver,url) == 2:
        if initialize.homepageD1(driver) == 1:
            #当在PPPOE环境下需要注释下面这行代码，该代码代替PPPOE环境
            if initialize.switch_PPPOE_DHCP_initialize(driver) == 1:
                return initialize.click_forget_password(driver)

#创建测试用例

class Test_click_forget_password:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_click_forget_password(self):
        assert click_forget_password(self.driver) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))