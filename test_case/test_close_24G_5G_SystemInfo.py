#-*- coding:utf-8 -*-

##################################
#   高级设置修改密码栏异常测试   #
##################################

import sys
import os
import pytest
import time
import configparser
from selenium import webdriver

#import测试库函数
sys.path.append("..")
from modules.login_router import *
from modules.router_setup import *
from modules.wifi import *

#创建测试对象
login = login_router()
router_s = router_setup()
config = configparser.ConfigParser()
wifi = wifi()
#获取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
login_password = config.get("Default","default_pw")
null_password = config.get("Password","null_pw")
long_password = config.get("Password","Illegal_long_pwd")
illegal_char_pwd = config.get("Password","Illegal_char")
chinese_char = config.get("Password","Chinese_char")
no_problem_pwd = config.get("Password","pass_pw")
error_pwd = config.get("Password","new_pw")
url = r"http://" + web_ip
#创建测试方法
#旧密码输入框输入空值
def check_close_24G_5G_SystemInfo(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,1) == 1:
                wifi.clickWiFi(driver,1)
                wifi.clickWiFi(driver,2)
                if router_s.setup_choose(driver,5) == 5:
                    return router_s.close_24G_5G_SystemInfo(driver)



#创建测试方法
class Test_systeminfo:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_close_24G_5G_SystemInfo(self):
        assert check_close_24G_5G_SystemInfo(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
