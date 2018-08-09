#-*- coding:utf-8 -*-

###########################
#   测试取消设置DHCP dns  #
###########################

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

#获取配置参数
path = os.path.dirname(os.getcwd())
config  = configparser.ConfigParser()
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
right_dns3 = config.get("Static","dns3")
right_dns4 = config.get("Static","dns4")
web_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_pw")
url = r"http://" + web_ip
default_dns3 = config.get("Static","dns3")
default_dns4 = config.get("Static","dns1")
#创建测试对象
login = login_router()
router_s = router_setup()

#创建测试方法
def check_cancel_set_dns(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if router_s.setup_choose(driver,2) == 2:
                if router_s.set_DHCP_dns_cancel(driver,right_dns3,right_dns4) == 1:
                    return router_s.get_default_DHCP(driver,default_dns3,default_dns4)

#创建测试用例
class Test_cancel_set_dhcp_dns:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_cancel_set_dns(self):
        assert check_cancel_set_dns(self.driver) == 1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))