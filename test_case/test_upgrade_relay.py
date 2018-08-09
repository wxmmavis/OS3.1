# -*- coding: utf-8 -*-
###################################
#   升级
#   配置在testconfig.ini中
###################################
import configparser
import logging
import os
import time
import shutil
import pytest
import conftest
#########################
#  import module
#########################
import sys
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.relay import *
from modules.initialize import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver
def case():
    lr = login_router()
    rs = router_setup()
    t = tools()
    r=relay()
    filename = os.path.basename(__file__).split('.')[0]
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
    test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    new_build = config.get('Upgrade', 'new_build')
    upgrade_wtime = int(config.get('Upgrade', 'upgrade_wtime'))
    wds_pw = config.get('WDS', 'wds_pw')
    ra0 = 1
    rai0 = 2
    driver = webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://'+default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 3) == 3:
                if r.clickRelay_D2(driver, "close") == 2:
                    if r.inputRelayPW(driver, wds_pw, ra0, 1) == 1:
                        time.sleep(10)
                        if rs.setup_choose(driver,5) == 5:
                            if rs.upgrade(driver, new_build, upgrade_wtime) == 1:
                                if lr.login(driver, default_pw) == 1:
                                    if rs.setup_choose(driver, 3) == 3:
                                        if tools().urlRequest("192.168.31.1") == 1:
                                            logging.info('===================Ping Success')
                                            driver.quit()
                                            return 1
                                        else:
                                            driver.get_screenshot_as_file(caseFail + "restartrelay-%s.jpg" % test_time)
                                            logging.warning("==================Ping Fail")
                                            return 2
    driver.quit()

def test_upgrade_relay():
    assert case()==1




if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))