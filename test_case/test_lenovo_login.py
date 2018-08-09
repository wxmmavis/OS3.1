#-*- coding:utf-8 -*-

import pytest
from selenium import webdriver
import sys
import os
import time
import configparser

sys.path.append("..")
import modules.login_lenovo

import modules
from modules.login_lenovo import *

#读取配置文件
config = configparser.ConfigParser()
path = os.path.dirname(os.getcwd())
config.read(path + r"\lenovo_config\lenovo.ini",encoding="utf-8")
url = config.get("login_web","login_url")
pwd = config.get("login_web","r_password")
type = config.get("login_web","open_type")
guide_type = config.get("login_web","guide_type")
password_null = config.get("login_web","password_null")
password_error = config.get("login_web","password_error")
times = config.get("login_web","times")
time = config.get("login_web","time")
list_lecoo = config.get("login_web","list_lecoo")
list_weixin = config.get("login_web","list_weixin")
list_weibo = config.get("login_web","list_weibo")
list_service = config.get("login_web","list_service")

#创建一个对象
login = login_lenovo()
#打开路由器登录页
def open_router(driver):
    return login.open_url(url,driver,type)
#打开设置向导首页
def open_guide_web(driver):
    return login.open_url(url,driver,guide_type)
#输入正常的账号并登录
def login_router(driver):
    if login.open_url(url,driver,type) == 1:
        return login.login_router(driver,pwd)
#输入账号为空
def input_null_password(driver):
    if login.open_url(url,driver,type) == 1:
        return login.abnormal_login(driver,password_null,time)
#输入错误的账号
def input_error_password(driver):
    if login.open_url(url,driver,type) == 1:
        return login.abnormal_login(driver,password_error,time)
#输入多次错误账号
def input_more_error_password(driver):
    if login.open_url(url,driver,type) == 1:
        return login.abnormal_login(driver,password_error,times)
#检查联想酷来官网链接
def check_footer_list_lecoo(driver):
    if login.open_url(url,driver,type) == 1:
        return login.footer(driver,list_lecoo)
#检查官方微信悬浮框
def check_footer_list_weixin(driver):
    if login.open_url(url,driver,type) == 1:
        return login.footer(driver,list_weixin)
#检查官方微博
def check_footer_list_weibo(driver):
    if login.open_url(url,driver,type) == 1:
        return login.footer(driver,list_weibo)
#检查服务网址（暂未上线）


class Test_open_url:
    def setup(self):
        self.driver = webdriver.Chrome()
    def teardown(self):
        self.driver.quit()
    # #测试打开网页
    # def test_open_router(self):
    #     assert open_router(self.driver) == 1
    # #测试打开初始化网页
    # def test_open_guide_web(self):
    #     assert open_guide_web(self.driver) == 1
    # #测试登录路由器
    # def test_login_router(self):
    #     assert login_router(self.driver) == 1
    # #测试输入为空的密码
    # def test_input_null_password(self):
    #     assert input_null_password(self.driver) == 2
    # #测试输入错误的密码
    # def test_input_error_password(self):
    #     assert input_error_password(self.driver) == 1
    #测试输入多次错误密码
    def test_input_more_error_password(self):
        assert input_more_error_password(self.driver) == 3
    # #测试点击联想来酷链接
    # def test_check_footer_list_lecoo(self):
    #     assert check_footer_list_lecoo(self.driver) == 1
    # #测试点击官方微信链接
    # def test_check_footer_list_weixin(self):
    #     assert check_footer_list_weixin(self.driver) == 2
    # #测试点击官方微博链接
    # def test_check_footer_list_weibo(self):
    #     assert check_footer_list_weibo(self.driver) == 3
    # #测试点击服务网址链接（未上线）

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))





