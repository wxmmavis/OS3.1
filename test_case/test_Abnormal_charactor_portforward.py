#-*- coding:utf-8 -*-
################################
#   端口转发输入框异常输入检查   #
################################

import sys
import os
import pytest
import time
import configparser
from selenium import webdriver

#import测试库函数
sys.path.append("..")
from modules.login_router import *
from modules.advanced_setup import *

#创建测试对象
login = login_router()
advanced_setup = advanced_setup()
config = configparser.ConfigParser()
#读取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="UTF-8")
web_ip = config.get("Default","default_ip")
url = r"http://" + web_ip
pwd = config.get("Default","default_pw")
username_null = config.get("Port_Forward","username_null")
username_over_long = config.get("Port_Forward","username_over_long")
address_null = config.get("Port_Forward","ip_address")
address_abnormal = config.get("Port_Forward","ip_address_abnormal")
address_abnormal_list = address_abnormal.split()
first_portforward_outports = config.get("Port_Forward","first_portforward_outports")
first_portforward_outports_list = first_portforward_outports.split()
second_portforward_outports = config.get("Port_Forward","second_portforward_outports")
second_portforward_outports_list = second_portforward_outports.split()
first_portforward_insideports = config.get("Port_Forward","first_portforward_insideports")
first_portforward_insideports_list = first_portforward_insideports.split()
second_portforward_insideports = config.get("Port_Forward","second_portforward_insideports")
second_portforward_insideports_list = second_portforward_insideports.split()
portforward_outport = config.get("Port_Forward","portforward_outport").split()
autoname = config.get("Port_Forward","autoname")
portSection = config.get("Port_Forward","portSection_TCP")
last_ip = config.get("DMZ","dmz_ip")
outport = config.get("Port_Forward","portforward_outport")
inport = config.get("Port_Forward","portforward_inport")
state_y = config.get("Port_Forward","state_y")
state_n = config.get("Port_Forward","state_n")
action_save = config.get("Port_Forward","action_save")
#创建测试方法
#输入为空的端口转发名称
def check_input_null_username(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_character_Portforward_usrname(driver,username_null)
#输入超长的端口转发名称
def check_input_username_over_long(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_character_Portforward_usrname(driver,username_over_long)
#输入空的端口转发IP地址
def check_input_null_Portforward_address(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_character_Portforward_address(driver,address_abnormal_list)
#输入异常的端口转发IP地址
def check_input_Abnormal_character_Portforward_address(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_character_Portforward_address(driver)

#外部端口第一个输入框输入为空
def check_input_null_portforward_outside_port(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_outportt(driver)

#外部端口第一个输入框输入异常值
def check_input_Abnormal_character_Portforward_outside_port(driver):
     if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_outportt(driver,first_portforward_outports_list)

#外部端口第二个输入框输入异常值
def check_input_Abnormal_character_Portforward_outside_port_second(driver):
     if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_outportt(driver,portforward_outport,second_portforward_outports_list)


#内部端口第一个输入框输入为空
def check_input_null_portforward_inside_port(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_insideport(driver)

#内部端口第一个输入框输入异常值
def check_input_Abnormal_character_Portforward_inside_port(driver):
     if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_insideport(driver,first_portforward_outports_list)

#内部端口第二个输入框输入异常值
def check_input_Abnormal_character_Portforward_inside_port_second(driver):
     if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                return advanced_setup.input_Abnormal_insideport(driver,portforward_outport,second_portforward_outports_list)
#输入相同的外部端口号(生效)
def input_Port_conflict_portforward_state_y(driver):
     if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                if advanced_setup.click_newbutton(driver) == 1:
                    if advanced_setup.set_newportfoward(driver,autoname,portSection,last_ip,outport,inport,state_y) == 1:
                        if advanced_setup.save_cancel_portforward(driver,action_save):
                            if advanced_setup.click_newbutton(driver) == 1:
                                advanced_setup.set_newportfoward(driver,autoname,portSection,last_ip,outport,inport,state_y)
                                advanced_setup.save_cancel_portforward(driver,action_save)
                                return advanced_setup.Port_conflict_portforward(driver)
#输入相同的外部端口号(不生效)
def input_Port_conflict_portforward_state_n(driver):
     if login.open_url(driver,url) == 1:
        if login.login(driver,pwd) == 1:
            if advanced_setup.adsetupChoose(driver) == 1:
                if advanced_setup.click_newbutton(driver) == 1:
                        advanced_setup.set_newportfoward(driver,autoname,portSection,last_ip,outport,inport,state_n)
                        advanced_setup.save_cancel_portforward(driver,action_save)
                        return advanced_setup.Port_conflict_portforward(driver)
#创建测试用例
class Test_Abnormal_charactor_portforward:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_input_null_username(self):
        assert check_input_null_username(self.driver) == 1

    def test_check_input_username_over_long(self):
        assert check_input_username_over_long(self.driver) == 2

    def test_check_input_null_Portforward_address(self):
        assert check_input_null_Portforward_address(self.driver) == 1

    def test_check_input_Abnormal_character_Portforward_address(self):
        assert check_input_Abnormal_character_Portforward_address(self.driver) == 1

    def test_check_input_null_portforward_outside_port(self):
        assert check_input_null_portforward_outside_port(self.driver) == 1

    def test_check_input_Abnormal_character_Portforward_outside_port(self):
        assert check_input_Abnormal_character_Portforward_outside_port(self.driver) == 1

    def test_check_input_Abnormal_character_Portforward_outside_port_second(self):
        assert check_input_Abnormal_character_Portforward_outside_port_second(self.driver)

    def test_check_input_null_portforward_inside_port(self):
        assert check_input_null_portforward_inside_port(self.driver) == 1

    def test_check_input_Abnormal_character_Portforward_inside_port(self):
        assert check_input_Abnormal_character_Portforward_inside_port(self.driver) == 1

    def test_check_input_Abnormal_character_Portforward_inside_port_second(self):
        assert check_input_Abnormal_character_Portforward_inside_port_second(self.driver)
    def test_input_Port_conflict_portforward_state_y(self):
        assert input_Port_conflict_portforward_state_y(self.driver) == 1
    def test_input_Port_conflict_portforward_state_n(self):
        assert input_Port_conflict_portforward_state_n(self.driver) == 1

if __name__ == "__main__":
    pytest.main(os.path.basename(__file__))