# -*- coding: utf-8 -*-

import logging
import time
import os
from tools import *
from selenium .webdriver.common.action_chains import ActionChains

class relay:
    def relay(self, driver):
        time.sleep(2)
        try:
            logging.info("=== Try Relay ===")
            driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(3) > a > span").click()
            time.sleep(5)
            getRe = driver.find_element_by_css_selector("#sectionitem_wds > div > p").text
            logging.info("get Relay = %s" % getRe)
            print(getRe)
            if getRe == '无线中继未开启！':
                return 1
            else:
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/Relay-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("=== Enter Relay Fail === %s" % e)
            return 0
        finally:
            pass


    def clickRelay(self, driver):
        time.sleep(2)
        try:
            time.sleep(30)
            logging.info("=== Click Relay BTN ===")
            driver.find_element_by_css_selector("#section_system_wds > div > div > div.section-switch.dmz-switch.switch-off").click()
            time.sleep(30)
            try:
                logging.info("check huawei")
                driver.find_element_by_id("undefined_Xiaomi_test").is_displayed()
                logging.info('check success')
                if tools().urlRequest('192.168.31.1') == 1:
                    logging.info('=== Ping OK ===')
                    return 1
                else:
                    ##失败
                    logging.info('=== Ping Fail===')
                    return 2
            except:
                return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/clickRelay-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("=== Click Relay BTN ERROR=== %s" % e)
            return 0
        finally:
            pass


    def clickRelay_D2(self, driver,btn):
        time.sleep(2)
        try:
            time.sleep(30)
            logging.info("=== Click Relay BTN ===")
            if btn=="close":
                driver.find_element_by_css_selector("#section_system_wds > div > div > div.section-switch.dmz-switch.switch-off").click()
            if btn=="open":
                driver.find_element_by_css_selector("#section_system_wds > div > div > div.section-switch.dmz-switch.switch-on").click()
            time.sleep(60)
            try:
                logging.info("check huawei")
                driver.find_element_by_id("undefined_Xiaomi_test_5G").is_displayed()
                logging.info('check success')
                if tools().urlRequest('192.168.31.1') == 1:
                    logging.info('=== Ping OK ===')
                    return 1
                else:
                    ##失败
                    logging.info('=== Ping Fail===')
                    return 2
            except:
                return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/clickRelay-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("=== Click Relay BTN ERROR=== %s" % e)
            return 0
        finally:
            pass


    def inputRelayPW(self, driver, wds_pw, relChoose, wdsChoose):
        time.sleep(30)
        logging.info("=== Input Relay Password ===")
        try:
            if relChoose ==1:
                logging.info("Choose 2.4G relay")
                driver.find_element_by_id("undefined_Xiaomi_test").click()
            if relChoose ==2:
                logging.info("Choose 5G relay")
                driver.find_element_by_id("undefined_Xiaomi_test_5G").click()
            time.sleep(5)
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div > div > input").send_keys(wds_pw)
            time.sleep(2)
            if wdsChoose == 1:
                logging.info('Sure')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            if wdsChoose == 2:
                logging.info('Cancel')
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-cancel").click()
            time.sleep(30)
            if tools().urlRequest('192.168.31.1') == 1:
                logging.info('=== Ping OK===')
                return 1
            else:
                logging.info('=== Ping Fail===')
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/inputRelay-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("=== Input Relay Password Fail === %s" % e)
            return 0
        finally:
            pass


    def clearRelay(self, driver, relChoose, clearChoose):
        time.sleep(30)
        logging.info("=== Clear Relay ===")
        try:
            if relChoose == 1:
                driver.find_element_by_id("undefined_Xiaomi_test").click()
            if relChoose == 2:
                driver.find_element_by_id("undefined_Xiaomi_test_5G").click()
            time.sleep(5)
            if clearChoose == 1:
                logging.info("Sure Clear")
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            if clearChoose == 2:
                logging.info("Cancel Clear")
                driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-cancel").click()
            time.sleep(15)
            if  tools().urlRequest('192.168.31.1') == 1:
                logging.info('=== Ping OK===')
                return 1
            else:
                logging.info('=== Ping Fail===')
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/clearRelay-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("=== Clear Relay Fail === %s" % e)
            return 0
        finally:
            pass


    def errorSure(self,driver):
        time.sleep(2)
        logging.info("=== Error Sure Relay ===")
        try:
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div").click()
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/errorSure-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            logging.warning("=== error Sure Fail === %s" % e)
            return 0
        finally:
            pass

####输入错误密码#######
    def relay_errorPW(self,driver):
        time.sleep(30)
        logging.info("=== Input Relay Password ===")
        try:
            logging.info("Choose 2.4G relay")
            driver.find_element_by_id("undefined_Xiaomi_test_5G").click()
            logging.info('Sure')
            time.sleep(5)
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div > div > input").send_keys("12154611")
            time.sleep(2)
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            time.sleep(120)
            getRe=driver.find_element_by_css_selector("body > div.modal.fade.pop-modal.wide.in > div > div > div.modal-body.pop-body > div > p > div > div > div:nth-child(1) > p.section-help-key").text
            if getRe == "1. 收到信号,却无法上网：":
                return 1
            else:
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(
                os.path.dirname(os.getcwd()) + "/errorpng/inputRelay-%s.jpg" % time.strftime("%Y%m%d%H%M%S",
                                                                                             time.localtime()))
            logging.warning("=== Input Relay Password Fail === %s" % e)
            return 0
        finally:
            pass

####检查DHCP##########
    def restore_DHCP(self,driver):
        time.sleep(2)
        try:
            time.sleep(3)
            logging.info("check dhcp")
            getRe=driver.find_element_by_css_selector("#section-pane-sysinfo > div > div.luci2-field-widget > div.info-view > div:nth-child(1) > span.line-right").text
            if getRe == "DHCP":
                return 1
            else:
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(
                os.path.dirname(os.getcwd()) + "/errorpng/inputRelay-%s.jpg" % time.strftime("%Y%m%d%H%M%S",
                                                                                             time.localtime()))
            logging.warning("=== check dhcp Fail === %s" % e)
            return 0
        finally:
            pass

#########中继相同ip#########
    def relay_sameIP(self,driver):
        time.sleep(30)
        try:
            logging.info("Choose 2.4G relay")
            driver.find_element_by_id("undefined_LecooNewifi_6a69").click()
            logging.info('Sure')
            time.sleep(5)
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-body.pop-body > div > div > input").send_keys("12345678")
            time.sleep(2)
            driver.find_element_by_css_selector("body > div.modal.fade.wide.in > div > div > div.modal-foot.pop-foot > div > div.newifi-btn.btn-sure").click()
            time.sleep(60)
            getre=driver.find_element_by_css_selector("body > div.modal.fade.pop-modal.wide.in > div > div > div.modal-body.pop-body > div > div > p:nth-child(1)").text
            if getre == "本路由与上级路由网关相同，无法进行中继":
                return 1
            else:
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(
                os.path.dirname(os.getcwd()) + "/errorpng/inputRelay-%s.jpg" % time.strftime("%Y%m%d%H%M%S",
                                                                                             time.localtime()))
            logging.warning("=== Input Relay Password Fail === %s" % e)
            return 0
        finally:
            pass

