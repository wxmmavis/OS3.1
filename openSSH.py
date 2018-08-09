# -*- coding: utf-8 -*-

import configparser
import logging
import os
import sys
import time
import csv
from tools import *
from modules.login_router import *
from selenium import webdriver



def do_test(driver, config_file):
    lr = login_router()
    t = tools()
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    for i in range(10):
        driver.get('http://' + default_ip + '/newifi/ifiwen_hss.html')
        time.sleep(3)
        if driver.find_element_by_css_selector("body").text == 'success':
            logging.info("OPEN SSH")
            logging.shutdown()
            break
        else:
            logging.error("OPEN SSH fail")


if __name__ == '__main__':
    chrome = webdriver.Chrome()
    projectpath = os.getcwd()
    do_test(chrome, projectpath + '\\configure\\' + 'testconfig.ini')
    chrome.close()