#-*- coding:utf-8 -*-

###################################
#   通过外网域名跳转到初始化首页  #
###################################

#import 库函数
import sys
import os
import pytest
#import time
import configparser
from selenium import webdriver

#import测试库
sys.path.append("..")
from modules.login_router import *
#from modules.initialize_d2l import *

#创建对象
login = login_router()
config = configparser.ConfigParser()

#获取配置
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding = "utf-8")
domain_name = config.get("Default","domain_name")
url = r"http://" + domain_name
#测试方法
def input_domain_name_jump_initialize(driver):
    time.sleep(120)
    return login.open_url(driver,url)


#创建测试用例
class Test_jump_initialize:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_input_domain_name_jump_initialize(self):
        assert input_domain_name_jump_initialize(self.driver) == 2

if __name__ == "__main__":
    pytest.main(os.path.basename(__file__))