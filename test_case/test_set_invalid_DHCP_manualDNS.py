#-*- coding:utf-8 -*-

###########################################
#   DHCO手动DNS，第一个无效，第二个有效   #
###########################################

import sys
import os
import time
import pytest
import configparser
from selenium import webdriver

#import 测试库函数

sys.path.append("..")
from modules.login_router import *
from modules.router_setup import *

#创建测试对象

login = login_router()
router_s = router_setup()
config = configparser.ConfigParser()

#获取配置文件
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
pwd = config.get("Default","default_pw")
invalid_dns1 = config.get("Static","dns3")
valid_dns2 = config.get("Static","dns1")
url = r"http://" + web_ip

#创建测试方法
def check_set_invalid_DHCP_manualDNS(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) ==1:
            if router_s.setup_choose(driver,2) == 2:
                if router_s.setDHCP(driver,1,invalid_dns1,valid_dns2) == 1:
                    driver.get("http://www.baidu.com")
                    value = driver.find_element_by_id("su").get_attribute("value")
                    time.sleep(2)
                    if value == "百度一下":
                        return 1

#创建测试用例
class Test_invalid_dns:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_set_invalid_DHCP_manualDNS(self):
        assert check_set_invalid_DHCP_manualDNS(self.driver) == 1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
