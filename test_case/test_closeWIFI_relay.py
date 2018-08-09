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
    projectpath = os.path.dirname(os.getcwd())
    caseFail = os.path.dirname(os.getcwd()) + '/errorpng/caseFail/'
    test_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')

    driver=webdriver.Chrome()
    if lr.open_url(driver, 'http://' + default_ip) == 1:
        if lr.login(driver, default_pw) == 1:
            if rs.setup_choose(driver,1)==1:
                try:
                    time.sleep(2)
                    logging.info("close wifi")
                    driver.find_element_by_id('section_switch_ra0').click()
                    time.sleep(15)
                    driver.find_element_by_id("section_switch_rai0").click()
                    time.sleep(15)
                    rs.setup_choose(driver,3)
                    time.sleep(3)
                    driver.find_element_by_css_selector("#section_system_wds > div > div > div.section-switch.dmz-switch.switch-off").click()
                    time.sleep(5)
                    getRe=driver.find_element_by_css_selector("#undefined_wds-not-have > p").text
                    print(getRe)
                    if getRe == "WIFi设置尚未开启，无法进行无线中继!":
                        logging.info("close wifi to relay success")
                        return 1
                    else:
                        return 2
                except Exception as e:
                    driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/error/closeWIFIrelay-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
                    logging.warning('=== close wifi to relay success ===%s' % e)
                    return 0
                finally:
                    pass


def test_closeWIFI_relay():
    assert case()==1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))


