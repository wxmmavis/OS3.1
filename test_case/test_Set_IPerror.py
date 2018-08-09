import configparser
import logging
import os
import time
import paramiko
import pytest
#########################
#  import module
#########################
import sys
import conftest
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver


lr=login_router()
rs=router_setup()
t=tools()
projectpath = os.path.dirname(os.getcwd())
caseFail = projectpath + '/errorpng/caseFail/'
test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
filename = os.path.basename(__file__).split('.')[0]
t.log(filename)
logging.info(__file__)
config_file = projectpath + '/configure/' + 'testconfig.ini'
config = configparser.ConfigParser()
config.read(config_file, encoding='UTF-8')
default_ip=config.get("Default",'default_ip')
default_pw=config.get("Default",'default_pw')

########输入不合法IP地址########
def set_errorIP(driver):
    if rs.set_failIP(driver) == 1:
        return 1

#########输入不合法IP范围##############
def set_errorIP_scope(driver):
    if rs.set_errorIPscope(driver)==1:
        return 1
#########输入不合法租约时间##############
def set_errorTime(driver):
    if rs.set_errorTime(driver)==1:
        return 1
##########不做修改点击保存#########
def save_Error(driver):
    if rs.saveError(driver)==1:
        return 1

##########关闭DHCP服务后不能获取IP范围和租约时间
def close_DHCP(driver):
    if rs.closeDHCP(driver)==0:
        return 1

class Test_errorIP:
    def setup(self):
        conftest.browser()
        self.driver = conftest.driver
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        if  lr.open_url(self.driver,"http://"+default_ip)==1:
            if lr.login(self.driver,default_pw)==1:
                if rs.setup_choose(self.driver,4)==4:
                    pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_setfail_IP(self):
        assert set_errorIP(self.driver)==1


    def test_seterrorIP_scope(self):
        assert set_errorIP_scope(self.driver)==1

    def test_setError_Time(self):
        assert set_errorTime(self.driver)==1

    def test_saveError(self):
        assert save_Error(self.driver)==1

    def test_closeDHCP(self):
        assert close_DHCP(self.driver)==1



if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
