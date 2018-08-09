# -*- coding:utf-8 -*-
###################################
#   初始化配置
###################################
import logging
import time
import os

class initialize:
    ###初始化首页-new###
    def homepage(self, driver):
        time.sleep(10)
        try:
            logging.info("Initialize configuration")
            driver.find_element_by_id("check-btn").click()
            time.sleep(30)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/homepage%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("enter initialize fail %s" % e)
            return 0

    def homepageD1(self, driver):
        time.sleep(3)
        try:
            logging.info("=== Try Click Agree ===D1")
            driver.find_element_by_css_selector("#initalize-protocol > div > label").click()
            logging.info("Initialize configuration")
            time.sleep(15)
            driver.find_element_by_id("check-btn").click()
            time.sleep(30)
            for i in range(2):
                try:
                    if driver.find_element_by_xpath("//p[text()='无法检测到网络']").is_displayed():
                        logging.error("==============无法检测到网络================")
                        driver.find_element_by_xpath("//a[text()='返回']").click()
                        time.sleep(5)
                        driver.find_element_by_id("check-btn").click()
                        time.sleep(20)
                except:
                    pass
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/homepage%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.error("enter initialize fail %s" % e)
            return 0
        finally:
            pass


    ###判断网络类型###
    def detect_wan(self, driver):
        flag = ['运营商', 'DHCP']
        try:
            tip = str(driver.find_element_by_css_selector("p.tips-text").text)
            for i in flag:
                if tip.find(i) > -1:
                    print(i)
                    if i == 'DHCP':
                        return 1
                    elif i == '运营商':
                        return 2
                    else:
                        return 3
        except Exception as e:
            logging.error("detect wan fail %s" % e)
            return 0


    ###DHCP###
    def detection_dhcp(self, driver):
        time.sleep(3)
        try:
            logging.info('try DHCP configuration')
            time.sleep(25)
            driver.find_element_by_css_selector("body > div.main > a").click()
            logging.info('detection DHCP success')
            time.sleep(5)
            try:
                driver.find_element_by_id("key").is_displayed()
                return 1
            except:
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/detection_DHCP-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning('detection fail %s' % e)
            return 0


    ####WAN口未连接网线####
    def initialize_skip(self, driver):
        time.sleep(15)
        try:
            #driver.find_element_by_link_text(u"跳过检测").click()
            time.sleep(3)
            driver.find_element_by_id("key").clear()
            time.sleep(3)
            driver.find_element_by_id("key").send_keys("12345678")
            time.sleep(3)
            driver.find_element_by_id("wifi").click()
            time.sleep(10)
            #driver.find_element_by_link_text(u"登录路由器").click()
            time.sleep(10)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/initialize_skip-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize skip fail %s" % e)
            return 0


    ####WAN口连接PPPOE网线-new####
    def detection_pppoe(self, driver, pppoe_user, pppoe_pw):
        time.sleep(30)
        try:
            #driver.find_element_by_class_name("btn").click()
            #time.sleep(3)
            logging.info("pppoe configuration")
            driver.find_element_by_id("broadband").clear()
            driver.find_element_by_id("broadband").send_keys(pppoe_user)
            time.sleep(1)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(pppoe_pw)
            time.sleep(3)
            driver.find_element_by_id("pppoe-btn").click()
            time.sleep(60)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/detection-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("initialize pppoe fail  %s" % e)
            return 0


    ####初始化配置wifi密码-new####
    def initialize_pw(self, driver, default_pw):
        time.sleep(15)
        try:
            logging.info('=== Click PASSWORD BTN ===')
            driver.find_element_by_id("input-showpwd-btn").click()
            time.sleep(1)
            logging.info("=== Try Set WiFi Password ===")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(default_pw)
            time.sleep(3)
            logging.info("save initialize password == %s" % default_pw)
            driver.find_element_by_id("wifi-btn").click()
            logging.info("set initialize password success")
            try:
                time.sleep(5)
                driver.find_element_by_css_selector("#layui-m-layer0 > div.layui-m-layermain > div > div > div.layui-m-layerbtn > span").is_displayed()
                driver.find_element_by_css_selector("#layui-m-layer0 > div.layui-m-layermain > div > div > div.layui-m-layerbtn > span").click()
                time.sleep(5)
            except:
                pass
            time.sleep(15)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/initialize_pw-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("initialize set wifi fail %s" % e)
            return 0


    ####设置wifi SSID####
    def setssid(self, driver, test_wifi):
        time.sleep(2)
        try:
            logging.info("initialize set wifi ssid ")
            driver.find_element_by_id("wifi")
            driver.find_element_by_id("wifi").clear()
            time.sleep(1)
            driver.find_element_by_id("wifi").send_keys(test_wifi)
            time.sleep(3)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/setssid-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize set wifi SSID fail %s" % e)
            return 0


    ####获取wifi SSID####
    def getssid(self, driver,test_ssid):
        try:
            #driver.find_element_by_id("ssid")
            getSSID_value=driver.find_element_by_id("wifi").get_attribute("value")
            logging.info(getSSID_value)
            time.sleep(1)
            if getSSID_value == test_ssid:
                logging.info('get SSID %s = %s' % (getSSID_value,test_ssid))
                return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/getssid-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize get wifi ssid fail %s" % e)
            return 0


    def setPW(self,driver,test_pw):
        time.sleep(15)
        try:
            logging.info('=== Click PASSWORD BTN ===')
            driver.find_element_by_id("input-showpwd-btn").click()
            time.sleep(1)
            logging.info("=== Try Set WiFi Password ===")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(test_pw)
            time.sleep(3)
            logging.info("save initialize password == %s" % test_pw)
            driver.find_element_by_id("wifi-btn").click()
            logging.info("set initialize password success")
            try:
                time.sleep(5)
                driver.find_element_by_css_selector("#layui-m-layer0 > div.layui-m-layermain > div > div > div.layui-m-layerbtn > span").is_displayed()
                driver.find_element_by_css_selector("#layui-m-layer0 > div.layui-m-layermain > div > div > div.layui-m-layerbtn > span").click()
                time.sleep(5)
            except:
                return 2
            time.sleep(15)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/initialize_pw-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("initialize set wifi fail %s" % e)
            return 0


    ###完成初始化配置-new###
    def complete(self, driver):
        time.sleep(2)
        try:
            #driver.find_element_by_css_selector("body > div.main > a").click()
            #time.sleep(5)
            logging.info("=== Complete Initialize ===")
            driver.find_element_by_id("finish-btn").click()
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/complete-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("=== initialize complete fail === %s" % e)
            return 0


    ###获取初始化首页文本###
    def texthome(self, driver):
        try:
            texthomes=driver.find_element_by_class_name("init-text").text
            logging.info(texthomes)
            if texthomes == "欢迎体验newifi 路由器，请简单设置完成初始化配置":
                logging.info("welcome case success!")
            else:
                logging.warning("get welcome fail")
            ######
            texthomes2=driver.find_element_by_class_name("init-protocol-text").text
            logging.info(texthomes2)
            if texthomes2 == "我已阅读并同意《newifi 路由器用户协议》和《搜狐共享服务协议》，并同意开启搜狐视频加速服务。":
                logging.info("agreement case success!")
            else:
                logging.warning("get agreement fail")
            ###左边栏###
            lefttext=driver.find_element_by_class_name("aside-content").text
            logging.info(lefttext)
            if lefttext == "初始化":
                logging.info("left case success!")
            else:
                logging.warning("get left fail")
            return 1
        except Exception as e:
            logging.warning("get initialize home fail %s" % e)
            return 0


    ###获取WIFI设置页面文本内容###
    def textwifi(self, driver):
        ###获取-wifi设置###
        lefttext=driver.find_element_by_class_name("aside-content").text
        print(lefttext)
        ###获取-请输入WiFi名称和密码###
        textsp=driver.find_element_by_css_selector("body > div.main > table > thead > tr > th:nth-child(2)").text
        print(textsp)
        ###获取-初始化设置WiFi密码将作为路由器登录密码###
        textpp=driver.find_element_by_class_name("form-text").text
        print(textpp)

####在设置初始化成功前关闭网页####
    def close_initialize(self, driver, default_pw):
        time.sleep(20)
        try:
            driver.find_element_by_id("password")
            driver.find_element_by_id("password").clear()
            time.sleep(1)
            driver.find_element_by_id("password").send_keys(default_pw)
            time.sleep(3)
            logging.info("save initialize password == %s" % default_pw)
            driver.find_element_by_id("wifi-btn").click()
            time.sleep(3)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/close_initialize-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("close initialize set wifi fail %s" % e)
            return 0
        finally:
            pass

###PPPOE&DHCP转换###
    def switch_PPPOE_DHCP_initialize(self,driver):
        time.sleep(10)
        try:
            #DHCP页面跳转到PPPOE页面
            if driver.find_element_by_id("wifi-footer-left").is_displayed():
                driver.find_element_by_id("wifi-footer-left").click()
                time.sleep(2)
                if driver.find_element_by_xpath("//p[text()='请输入运营商宽带账号']").is_displayed():
                    return 1
        except:
            pass
        try:
            #PPPOE页面跳转到DHCP页面
            if driver.find_element_by_css_selector("#wrap > div.footer.form-footer > a:nth-child(1)").is_displayed():
                driver.find_element_by_css_selector("#wrap > div.footer.form-footer > a:nth-child(1)").click()
                time.sleep(2)
                if driver.find_element_by_xpath("//p[text()='请设置WiFi名称和密码']").is_displayed():
                    return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/switch_PPPOE_DHCP_initialize-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("switch_PPPOE_DHCP_initialize fail %s" % e)
            return 0
###PPPOE&DHCP转换###
    def switch_PPPOE_DHCP_initialize_D2l(self,driver):
        time.sleep(10)
        try:
            #DHCP页面跳转到PPPOE页面
            if driver.find_element_by_id("wifi-footer-left").is_displayed():
                driver.find_element_by_id("wifi-footer-left").click()
                time.sleep(2)
                if driver.find_element_by_xpath("//p[text()='请输入运营商宽带账号']").is_displayed():
                    return 1
        except:
            pass
        try:
            #PPPOE页面跳转到DHCP页面
            if driver.find_element_by_xpath("//a[text()='不需要拨号(DHCP)']").is_displayed():
                driver.find_element_by_xpath("//a[text()='不需要拨号(DHCP)']").click()
                time.sleep(2)
                if driver.find_element_by_xpath("//p[text()='请设置WiFi名称和密码']").is_displayed():
                    return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/switch_PPPOE_DHCP_initialize-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("switch_PPPOE_DHCP_initialize fail %s" % e)
            return 0
    ###PPPOE&DHCP页面返回初始化首页###
    def PPPOE_DHCP_comeback_initialize(self,driver):
        time.sleep(20)
        try:
            driver.find_element_by_xpath("//a[text()='返回']").click()
            time.sleep(1)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/PPPOE_DHCP_comeback_initialize-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("PPPOE_DHCP_comeback_initialize fail %s" % e)
            return 0

###PPPOE环境下,点击忘记密码###
    def click_forget_password(self,driver):
        time.sleep(20)
        try:
            driver.find_element_by_id("pppoe-forgetpwd-btn").click()
            driver.find_element_by_xpath("//div[@class='pppoe-popup']/p[1]").is_displayed()
            driver.find_element_by_xpath("//div[@class='pppoe-popup']/p[2]").is_displayed()
            driver.find_element_by_xpath("//div[@class='pppoe-popup']/p[3]").is_displayed()
            driver.find_element_by_xpath("//div[@class='pppoe-popup']/p[4]").is_displayed()
            driver.find_element_by_xpath("//div[@class='pppoe-popup']/p[5]").is_displayed()
            driver.find_element_by_xpath("//div[@class='pppoe-popup']/p[6]").is_displayed()
            driver.find_element_by_xpath("//div[@class='pppoe-popup']/p[7]").is_displayed()
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/click_forget_password_initialize-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("close initialize set wifi fail %s" % e)
            return 0
    ###联想固件PPPOE环境下，输入PPPOE账号密码###
    def input_pppoe_username_password_initialize_D2l(self,driver,username,password,illegal = None):
        time.sleep(20)
        try:
            driver.find_element_by_id("broadband").clear()
            driver.find_element_by_id("broadband").send_keys(username)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(password)
            driver.find_element_by_id("pppoe-btn").click()
            time.sleep(40)
            if illegal == None:
                driver.find_element_by_xpath("//p[@class='title']").is_displayed()
                return 1
            else:
                error_message = driver.find_element_by_id("error-message").text
                if error_message == "宽带账号或密码错误，请重新输入！":
                    return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/input_pppoe_username_password_initialize-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("close initialize set wifi fail %s" % e)
            return 0
    ###D2 PPPOE环境下，输入PPPOE账号密码###
    def input_pppoe_username_password_initialize(self,driver,username,password,illegal = None):
        time.sleep(20)
        try:
            driver.find_element_by_id("broadband").clear()
            driver.find_element_by_id("broadband").send_keys(username)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(password)
            driver.find_element_by_id("pppoe-btn").click()
            time.sleep(40)
            if illegal == None:
                driver.find_element_by_xpath("//p[@class='title']").is_displayed()
                return 1
            else:
                error_message = driver.find_element_by_id("error-message").text
                if error_message == "请联系运营商是否欠费或重启调制解调器(猫)再拨号！":
                    return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/input_pppoe_username_password_initialize-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("close initialize set wifi fail %s" % e)
            return 0

 ###获取默认SSID###
    def get_default_ssid(self, driver):
        try:
            js = "return document.getElementById('wifi').value;"
            texts  = driver.execute_script(js)
            logging.info(texts)
            time.sleep(1)
            logging.info("initialize get wifi default ssid success")
            return texts
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/getdefaultssid-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize get wifi default ssid fail %s" % e)
            return 0
        finally:
            pass

###设置非法的SSID####
    def set_Illegal_ssid(self,driver,Illegal_ssid,pwd):
        time.sleep(10)
        try:
            driver.find_element_by_id("wifi").clear()
            time.sleep(1)
            driver.find_element_by_id("wifi").send_keys(Illegal_ssid)
            driver.find_element_by_id("password").clear()
            time.sleep(1)
            driver.find_element_by_id("password").send_keys(pwd)
            driver.find_element_by_id("wifi-btn").click()
            error_msg = driver.find_element_by_id("error-message").text
            if error_msg == "WiFi名称只能由字母、英文字符、数字组成！":
                return 1
            elif error_msg == "WiFi名称请输入1-9位中文或者1-29位英文字符！":
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/set_Illegal_ssid-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize set set_Illegal_ssid fail %s" % e)
            return 0
    ####设置非法的初始化密码####
    def set_Illegal_password(self,driver,Illegal_pwd):
        time.sleep(10)
        try:
            driver.find_element_by_id("password").clear()
            time.sleep(1)
            driver.find_element_by_id("password").send_keys(Illegal_pwd)
            driver.find_element_by_id("wifi-btn").click()
            error_msg = driver.find_element_by_id("error-message").text
            if error_msg == "密码只能由字母、英文字符、数字组成！":
                return 1
            elif error_msg == "WiFi密码长度为8-64个字符！":
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/set_Illegal_pwd-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.warning("initialize set set_Illegal_pwd fail %s" % e)
            return 0

