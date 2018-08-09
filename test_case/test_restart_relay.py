# -*- coding: utf-8 -*-
import configparser
import logging
import os
import time
import csv
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
from modules.wifi import *
from modules.initialize import *
from modules.device_management import *
from modules.relay import *
from tools import *
#########################
from selenium import webdriver
def case():

    lr = login_router()
    rs = router_setup()
    t = tools()
    r = relay()
    w=wifi()
    projectpath = os.path.dirname(os.getcwd())
    caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
    test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    restart_wtime = int(config.get('Restart', 'restart_wtime'))
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')
    wds_pw = config.get('WDS', 'wds_pw')
    ra0 = 1
    driver=webdriver.Chrome()
    driver.maximize_window()
    if lr.open_url(driver, 'http://' + default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver, 3) == 3:
                if r.clickRelay_D2(driver, "close") == 2:
                    if r.inputRelayPW(driver, wds_pw, ra0, 1) == 1:
                        time.sleep(10)
                        if rs.setup_choose(driver, 5) == 5:
                            if rs.restart(driver, restart_wtime) == 1:
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

def test_restart_relay():
    assert case()==1


if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))
