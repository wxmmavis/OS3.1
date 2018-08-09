#-*- coding:utf-8 -*-

##################################
#   高级设置修改密码栏异常测试   #
##################################

import sys
import os
import pytest
import time
import configparser
from selenium import webdriver

#import测试库函数
sys.path.append("..")
from modules.login_router import *
from modules.router_setup import *

#创建测试对象
login = login_router()
router_s = router_setup()
config = configparser.ConfigParser()

#获取配置参数
path = os.path.dirname(os.getcwd())
config.read(path + r"\configure\testconfig.ini",encoding="utf-8")
web_ip = config.get("Default","default_ip")
login_password = config.get("Default","default_pw")
null_password = config.get("Password","null_pw")
long_password = config.get("Password","Illegal_long_pwd")
illegal_char_pwd = config.get("Password","Illegal_char")
chinese_char = config.get("Password","Chinese_char")
no_problem_pwd = config.get("Password","pass_pw")
error_pwd = config.get("Password","new_pw")
url = r"http://" + web_ip
#创建测试方法
#旧密码输入框输入空值
def check_old_password_null_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,null_password,null_password,null_password)
#旧密码输入框输入特殊字符
def check_old_password_illegal_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,illegal_char_pwd,null_password,null_password)
#旧密码输入框输入中文字符
def check_old_password_Chinese_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,chinese_char,null_password,null_password)
#新密码第一个输入框为空值
def check_new_password_01_null_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,no_problem_pwd,null_password,null_password)
#新密码第一个输入框为特殊字符
def check_new_password_01_illegal_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,no_problem_pwd,illegal_char_pwd,null_password)
#新密码第一个输入框为中文字符
def check_new_password_01_Chinese_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,no_problem_pwd,chinese_char,null_password)

#新密码第二个输入框为空值
def check_new_password_02_null_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,no_problem_pwd,no_problem_pwd,null_password)
#新密码第二个输入框为特殊字符
def check_new_password_02_illegal_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,no_problem_pwd,no_problem_pwd,illegal_char_pwd)
#新密码第二个输入框为中文字符
def check_new_password_02_Chinese_msg(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,no_problem_pwd,no_problem_pwd,chinese_char)
#输入错误的原始密码
def check_Modify_password_input_error_login_pwd(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_password_input_error_login_pwd(driver,error_pwd,no_problem_pwd,no_problem_pwd)
#新密码两次输入不一致
def check_input_not_equal_new_pwd(driver):
    if login.open_url(driver,url) == 1:
        if login.login(driver,login_password) == 1:
            if router_s.setup_choose(driver,5) == 5:
                return router_s.Modify_illegal_password(driver,no_problem_pwd,error_pwd,no_problem_pwd)
#创建测试方法
class Test_modify_password:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_check_old_password_null_msg(self):
        assert check_old_password_null_msg(self.driver) == 1
    def test_check_old_password_illegal_msg(self):
        assert check_old_password_illegal_msg(self.driver) == 2
    def test_check_old_password_Chinese_msg(self):
        assert check_old_password_Chinese_msg(self.driver) == 3
    def test_check_new_password_01_null_msg(self):
        assert check_new_password_01_null_msg(self.driver) == 4
    def test_check_new_password_01_illegal_msg(self):
        assert check_new_password_01_illegal_msg(self.driver) == 5
    def test_check_new_password_01_Chinese_msg(self):
        assert check_new_password_01_Chinese_msg(self.driver) == 6
    def test_check_new_password_02_null_msg(self):
        assert check_new_password_02_null_msg(self.driver) == 7
    def test_check_new_password_02_illegal_msg(self):
        assert check_new_password_02_illegal_msg(self.driver) == 8
    def test_check_new_password_02_Chinese_msg(self):
        assert check_new_password_02_Chinese_msg(self.driver) == 9
    def test_check_Modify_password_input_error_login_pwd(self):
        assert check_Modify_password_input_error_login_pwd(self.driver) == 1
    def test_check_input_not_equal_new_pwd(self):
        assert check_input_not_equal_new_pwd(self.driver) == 10
if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))