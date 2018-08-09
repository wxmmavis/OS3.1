# -*- coding:utf-8 -*-
###################################
#   登录路由管理页面
###################################
import logging
import time
import pytest
import os
from selenium.webdriver.support.ui import Select
# from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_argument('lang=en_US')
# driver = webdriver.Chrome(chrome_options = options)
class login_router:
    ###打开网址###
    def open_url(self, driver, url):
        ###返回1为欢迎界面，返回2为初始化界面####
        try:
            logging.info("try open " + url)
            driver.get(url)
            time.sleep(5)
            try:
                driver.find_element_by_class_name("login-logo").is_displayed()
                logging.info("enter welcome")
                return 1
            except:
                driver.find_element_by_id("check-btn").is_displayed()
                logging.info("enter initialize")
                return 2
            finally:
                pass
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/open_url%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===open url error=== %s", e)
            return 0
        finally:
            pass


    ####管理员密码登录###
    def login(self, driver, default_pw):
        time.sleep(2)
        try:
            logging.info("=== Login password === %s " % default_pw)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(default_pw)
            time.sleep(1)
            logging.info('click login btn')
            driver.find_element_by_css_selector("#sysauth > div > div > div.login-modal-content > div.modal-footer.login-modal-footer > div").click()
            time.sleep(5)
            try:
                ###检查是否登录成功,检测路由状态元素###
                logging.info('check login ')
                driver.find_element_by_css_selector("#mainmenu > ul > li.item-active > a > span").is_displayed()
                logging.info("login success")
                return 1
            except:
                logging.info("login fail")
                return 0
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/login%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===login error=== %s", e)
            return 0
        finally:
            pass


    def footer(self,driver):
        time.sleep(2)
        try:
            logging.info("test router footer")
            
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/footer-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("===test router footer error=== %s", e)
            return 0
        finally:
            pass


    #####页脚-官网#####
    def guanwang(self,driver):
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[2]/a")
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[2]/a").click()
        time.sleep(5)
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                time.sleep(2)
        guanwang_Actual_address = driver.current_url
        logging.info('=== Get Address === %s'% guanwang_Actual_address)
        guanwang_Standard_address = "http://www.newifi.com/"
        logging.info('=== GuanWang Address === %s'% guanwang_Standard_address)
        if guanwang_Actual_address == guanwang_Standard_address:
            logging.info("guanwang_ok")
            return 1
        else:
            logging.info("guanwang_faill")
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/guanwang-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0

    def guangwang1(self, driver):
           driver.find_element_by_css_selector("#navbar-text2").click()
           time.sleep(5)
           now_handle = driver.current_window_handle
           all_handles = driver.window_handles
           for handle in all_handles:
               if handle != now_handle:
                   driver.switch_to_window(handle)
                   time.sleep(2)
           guanwang_Actual_address = driver.current_url
           logging.info('=== Get Address === %s' % guanwang_Actual_address)
           guanwang_Standard_address = "http://www.xcloud.cc/"
           logging.info('=== GuanWang Address === %s' % guanwang_Standard_address)
           if guanwang_Actual_address == guanwang_Standard_address:
               logging.info("guanwang_ok")
               return 1
           else:
               logging.info("guanwang_faill")
               driver.get_screenshot_as_file(
                   os.path.dirname(os.getcwd()) + "/errorpng/guanwang-%s.jpg" % time.strftime("%Y%m%d%H%M%S",
                                                                                              time.localtime()))
               return 0


    #####页脚-微博#####
    def weibo(self,driver):
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[3]/a").click()
        time.sleep(10)
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                time.sleep(2)
        weibo_Actual_address = driver.current_url[:25]
        logging.info(weibo_Actual_address)
        weibo_Standard_address = "http://weibo.com/xyxcloud"
        logging.info(weibo_Standard_address)
        if weibo_Actual_address == weibo_Standard_address:
            logging.info("weibao_ok")
            return 1
        else:
            logging.info("weibao_faill")
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/weibo-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0

    def weibos(self, driver):
        weibo_url = driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[3]/a").get_attribute("href")
        logging.info('get weibo url = %s' % weibo_url)
        if weibo_url == 'http://weibo.com/xyxcloud?topnav=1&wvr=58&topsug=1':
            logging.info('weibo ====ok')
            return 1
        else:
            logging.error('weibo ===fail')
            return 0

    #####页脚-社区#####
    def shequ(self,driver):
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[5]/a")
        driver.find_element_by_xpath("//*[@id='footer']/div/ul/li[5]/a").click()
        time.sleep(5)
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                time.sleep(2)
        shequ_Actual_address = driver.current_url
        logging.info(shequ_Actual_address)
        shequ_Standard_address = "http://bbs.newifi.com/"
        logging.info(shequ_Standard_address)
        if shequ_Actual_address == shequ_Standard_address:
            logging.info("shequ_ok")
            return 1
        else:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/shequ-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("shequ_faill")
            return 0

#联想固件异常登录
    def abnormal_login(self,driver,password,times):
        try:
            time.sleep(2)
            logging.info("==============abnormal login===============")
            for i in range(int(times)):
                driver.find_element_by_id("login_password").clear()
                driver.find_element_by_id("login_password").send_keys(password)
                driver.find_element_by_xpath("//div[text()='登录']").click()
                time.sleep(1)
            login_warn = driver.find_element_by_xpath("//div[@class='login-warn']/p").text
            if login_warn == "输入密码错误，请重试！":
                logging.info("================error password test pass==============")
                return 1
            elif login_warn == "请输入密码！":
                logging.info("================null password test pass================")
                return 2
            elif login_warn == "输入错误次数过多，1小时内不能登录！":
                logging.info("================more error password test pass================")
                return 3
        except Exception as e:
            logging.error("================abnormal login test error================")
            driver.get_screenshot_as_file(self.path+r"\lenovo_png\abnormal_login_%s.png"%self.now_time)
            return 0


#联想固件酷来官网页脚链接
    def Official_network_url_d2l(self,driver,url):
        try:
            text = driver.find_element_by_xpath("//div[@id='footer']//li[1]/a").get_attribute("href")
            if text == url:
                logging.info("===============get Official_network_url suucess============= ")
                return 1
        except Exception as e:
            logging.error("===============get Official_network_url fail:%s============="%e)
            driver.get_screenshot_as_file(self.path+r"\lenovo_png\get_official_fail_%s.png"%self.now_time)
            return 0

    #联想固件微博官网页脚链接
    def weibo_url_d2l(self,driver,url):
        try:
            text = driver.find_element_by_xpath("//div[@id='footer']//li[2]/a").get_attribute("href")
            if text == url:
                logging.info("===============get weibo_url suucess============= ")
                return 1
        except Exception as e:
            logging.error("===============get weibo_url fail:%s============="%e)
            driver.get_screenshot_as_file(self.path+r"\lenovo_png\get_weibo_fail_%s.png"%self.now_time)
            return 0
    #联想固件检查服务网站页脚链接
    def service_url_d2l(self,driver,url):
        try:
            text = driver.find_element_by_xpath("//div[@id='footer']//li[3]/a").get_attribute("href")
            if text == url:
                logging.info("===============get service_url suucess============= ")
                return 1
        except Exception as e:
            logging.error("===============get service_url fail:%s============="%e)
            driver.get_screenshot_as_file(self.path+r"\lenovo_png\get_service_fail_%s.png"%self.now_time)
            return 0
    #联想固件检查官方微信网站页脚链接
    def weixin_url_d2l(self,driver,url):
        try:
            text = driver.find_element_by_xpath("//a[@id='weiMenu']/img").get_attribute("src")
            print(text)
            print(url)
            if text == url:
                logging.info("===============get weixin_url suucess============= ")
                return 1
        except Exception as e:
            logging.error("===============get weixin_url fail:%s============="%e)
            driver.get_screenshot_as_file(self.path+r"\lenovo_png\get_weixin_fail_%s.png"%self.now_time)
            return 0

#######首页底部mac
    def check_mac(self,driver,wan_mac):
        time.sleep(2)
        getRe=driver.find_element_by_css_selector("#footer > div > div > span.mac-address").text
        time.sleep(2)
        if getRe == wan_mac:
            return 1
        else:
            return 2

#######首页底部mac
    def check_version(self,driver,new_version):
        time.sleep(2)
        getRe=driver.find_element_by_css_selector("#footer > div > div > span.system-version").text
        time.sleep(2)
        if getRe == new_version:
            return 1
        else:
            return 2