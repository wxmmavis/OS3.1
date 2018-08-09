# -*- coding:utf-8 -*-
###################################
#  测试重启时WiFi启动
###################################
import configparser
import logging
import os
import pytest
import paramiko
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
from modules.initialize import *
from modules.device_management import *
from tools import *
#########################
from selenium import webdriver

def case():
    lr = login_router()
    rs = router_setup()
    t = tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    restart_count = int(config.get('Restart', 'restart_count'))
    default_ip = config.get('Default', 'default_ip')
    default_pw = config.get('Default', 'default_pw')

    driver = webdriver.Chrome()
    driver.get('http://'+default_ip+'/newifi/ifiwen_hss.html')
    driver.close()
    driver.quit()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(default_ip, 22, "root", default_pw)
    stdin, stdout, stderr = ssh.exec_command("ubus call xapi.system reboot '{}'")
    time.sleep(180)

    ssid_cmd = ['iwconfig ra0', 'iwconfig rai0']
    for ssid_cmd in ssid_cmd:
       lists = str.strip(t.ssh_cmdss(default_ip, default_pw, ssid_cmd)[1])
       logging.info(lists)
    if lists == 'Link Quality:0  Signal level:0  Noise level:0':
        logging.error('restart wifi close')
    else:
        logging.info('restart wifi open')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(default_ip, 22, "root", default_pw)
    stdin, stdout, stderr = ssh.exec_command("dmesg")
    logging.info(stdout.readlines())
    list3 = stdout.readlines()
    logging.info(list3)



for i in range(2):
    case()

