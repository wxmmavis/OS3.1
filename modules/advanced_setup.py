# -*- coding: utf-8 -*-
################
####高级设置####
################
import time
import os
import re
import logging
from time import ctime
from selenium.webdriver.common.keys import Keys

class advanced_setup:
    def adsetupChoose(self,driver):
        time.sleep(3)
        try:
            logging.info('======Advanced Setup ========')
            driver.find_element_by_xpath("//*[@id=\"mainmenu\"]/ul/li[5]/a/div").click()
            time.sleep(3)
            driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(1) > a > span").is_displayed()
            logging.info("enter advanced setup ok")
            return 1
        except  Exception  as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/adsetupChoose-%s.j pg" % ctime())
            logging.error('====adsetup Choose error==== %s' %e)
            return 0
        finally:
            pass


    def PortDMZ(self,driver):
        try:
            logging.info('======Port/DMZ Setup ========')
            driver.find_element_by_css_selector("#viewmenu > ul > li:nth-child(1) > a").click()
            time.sleep(3)
            driver.find_element_by_id("dmz_switch").is_displayed()
            logging.info("enter advanced setup ok")
            return 1
        except  Exception  as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/adsetupChoose-%s.jpg" % ctime())
            logging.error('====PortDMZ error==== %s' %e)
            return 0
        finally:
            pass


    def MACFiltering(self, driver):
        try:
            logging.info('============== MAC Filtering ==========')
            driver.find_element_by_css_selector('#viewmenu > ul > li:nth-child(2) > a').click()
            time.sleep(3)
            driver.find_element_by_id("mac_switch").is_displayed()
            logging.info('enter mac filtering ok')
            time.sleep(3)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/MACFiltering-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error('====MAC Filtering error==== %s' %e)
            return 0
        finally:
            pass


    def MacChoose(self, driver):
        try:
            return 1
        except Exception as e:
            return 0
        finally:
            pass


    def setBlack(self,driver):
        try:
            driver.find_element_by_css_selector('//*[@id="40331a7c4fa2"]/td[3]/div').click()
            time.sleep(5)
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/MACFiltering-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error('====MAC Filtering error==== %s' %e)
            return 0
        finally:
            pass


    def getBlack(self,driver):
        try:
            driver.find_element_by_css_selector('//*[@id="40331a7c4fa2"]/td[3]/div').click()
            time.sleep(5)
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/MACFiltering-%s.jpg" % time.strftime("%Y%m%d%H%M%S",time.localtime()))
            logging.error('====MAC Filtering error==== %s' %e)
            return 0
        finally:
            pass


    def getDMZ(self,driver):
        time.sleep(3)
        try:
            getdmz = driver.find_element_by_id("dmz_switch").get_attribute("class")
            logging.info("GET DMZ IP %s" % getdmz)
            if getdmz == "section-switch dmz-switch switch-off":
                logging.info("get DMZ IP status = NO")
                return 1
            else:
                logging.error("get DMZ status = YES")
                return 2
        except Exception as e:
            # driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/getDMZ-%s.jpg" % ctime())
            logging.error("==== GET DMZ ERROR %s===" % e)
            return 0
        finally:
            pass


    def clickDMZ(self,driver):
        try:
            logging.info('========= Click DMZ =========')
            driver.find_element_by_id("dmz_switch").click()
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/clickDMZ-%s.jpg" % ctime())
            logging.info("==== click DMZ ERROR %s===" % e)
            return 0
        finally:
            pass


    def getDMZIP(self, driver, dmz_ip,default_dmzip):
        time.sleep(2)
        try:
            logging.info("========= GET DMZ IP ===========")
            # jsDMZ = "return document.getElementByXpath('//*[@id=\"portdmz_dmz\"]/div[4]/div[2]/div/div[1]/div/input').value;"
            # getdmz = driver.execute_script(jsDMZ)
            getdmz = driver.find_element_by_xpath("//*[@id=\"portdmz_dmz\"]/div[4]/div[2]/div/div[1]/div/input").get_attribute("value")
            logging.info("GET DMZ IP %s" % getdmz)
            if getdmz == dmz_ip:
                logging.info("get DMZ IP = dmz ip")
                return 1
            elif getdmz == default_dmzip:
                logging.info("get DMZ IP = default dmz ip")
                return 2
            else:
                logging.error("get DMZ IP !=")
                return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/getDMZ-%s.jpg" % ctime())
            logging.error("==== GET DMZ ERROR %s===" % e)
            return 0
        finally:
            pass


    def setDMZ(self, driver, dmz_ip):
        time.sleep(2)
        try:
            logging.info("========= SET DMZ IP ========")
            driver.find_element_by_xpath("//*[@id=\"portdmz_dmz\"]/div[4]/div[2]/div/div[1]/div/input").clear()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"portdmz_dmz\"]/div[4]/div[2]/div/div[1]/div/input").send_keys(dmz_ip)
            logging.info("set dmz ip ===…%s" % dmz_ip)
            time.sleep(2)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/setDMZ-%s.jpg" % ctime())
            logging.error("===SET DMZ ERROR ===%s" % e)
            return 0
        finally:
            pass


    def check_DMZ_IP(self, driver, dmzip1):
        try:
            logging.info("========= Check DMZ IP========")
            get_dmzIp = driver.find_element_by_css_selector("dmz_ip_pre").text
            if get_dmzIp == dmzip1:
                logging.info("get DMZ IP = dmz ip")
                return 1
            elif get_dmzIp == dmzip1:
                logging.info("get DMZ IP = default dmz ip")
                return 2
            else:
                logging.error("get DMZ IP !=")
                return 3
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/check_DMZ_IP-%s.jpg" % ctime())
            logging.error("==== Check DMZ IP ERROR %s===" % e)
            return 0
        finally:
            pass


    def getDMZStatus(self, driver):
        try:
            get_DMZ_status = driver.find_element_by_css_selector("#portdmz_dmz > div.dmz-content > div.dmz-on > div > div:nth-child(2) > div > p").text
            if get_DMZ_status == u'生效' :
                logging.info(u'Status === 生效')
                return 1
            if get_DMZ_status == u'不生效':
                logging.info(u'Status === 不生效')
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/getDMZStatus-%s.jpg" % ctime())
            logging.error("==== check dmz status error==== %s" % e)
            return 0
        finally:
            pass


    def saveDMZ(self, driver):
        time.sleep(3)
        try:
            logging.info('click save dmz')
            driver.find_element_by_xpath("//*[@id=\"dmz_btn\"]").click()
            time.sleep(3)
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/saveDMZ-%s.jpg" % ctime())
            logging.error('save dmz error')
            return 0
        finally:
            pass


    #点击新增条目按钮
    def click_newbutton(self,driver):
        time.sleep(2)
        try:
            logging.info(u"============clcik new list============")
            driver.find_element_by_xpath("//span[text()='添加新条目']").click()
            time.sleep(2)
            return 1
        except Exception as e:
            logging.error (u"================error:click new list failed %s==================="%e)
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/clciknewbutton-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
        finally:
            pass

    #端口转发输入参数
    def set_newportfoward(self,driver,portSection_port_name,portSection,last_ip,outport,inport,state):
        try:
            logging.info(u"===========set new portfoward=========")
            driver.find_element_by_xpath("//input[@id='portSection2_port_name']").send_keys(portSection_port_name)
            driver.find_element_by_css_selector(".list-img").click()
            logging.info('change ')
            if portSection == 'TCP':
                driver.find_element_by_xpath("//span[@id='portSection2TCP']").click()
            elif portSection == 'UDP':
                driver.find_element_by_xpath("//span[@id='portSection2UDP']").click()
            elif portSection == 'TCP+UDP':
                driver.find_element_by_xpath("//span[@id='portSection2TCP+UDP']").click()
            else:
                logging.error(u"===============portSection set error=================")
            driver.find_element_by_xpath("//div[@id='portSection2_port_ip']//input[@type='text']").send_keys(last_ip)
            driver.find_element_by_xpath("//div[@id='portSection2_port_outside']//input[1]").send_keys(outport)
            driver.find_element_by_xpath("//div[@id='portSection2_port_inside']//input[1]").send_keys(inport)
            if state == '生效':
                driver.find_element_by_xpath("//label[text()='生效']").click()
            elif state == '不生效':
                driver.find_element_by_xpath("//label[text()='不生效']").click()
            else:
                logging.error(u"================portforward state set error=================")
            return 1
        except Exception as e:
            logging.error (u"================error:set new list failed %s==================="%e)
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/set_portforward-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 2
        finally:
            pass

    #保存或取消
    def save_cancel_portforward(self,driver,action):
        try:
            if action == '保存':
                driver.find_element_by_xpath("//div[text()='保存']").click()
                time.sleep(5)
            elif action == '取消':
                driver.find_element_by_xpath("//div[text()='取消']").click()
                time.sleep(5)
            return 1
        except Exception as e:
            logging.error(u"=============error: saver or cancel failed%s================="%e)
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/save_cancel-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 3
        finally:
            pass

    #检查规则
    def checkportforward(self,driver,portSection_port_name,portSection,last_ip,outport,inport,state,full_ip):
        try:
            time.sleep(5)
            now_name = driver.find_element_by_xpath("//p[@class='port-had-name']").text
            now_protocol = driver.find_element_by_xpath("//p[@class='port-had-protocol']").text
            now_ip = driver.find_element_by_xpath("//p[@class='port-had-ip']").text
            now_outport = driver.find_element_by_xpath("//p[@class='port-had-Outside']").text
            now_inport = driver.find_element_by_xpath("//p[@class='port-had-inside']").text
            now_state = driver.find_element_by_xpath("//p[@class='port-had-state']").text
        except Exception as e:
            logging.error(u"=============error: get value failed%s================="%e)
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/get_value-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 4
        try:
            if now_name == portSection_port_name:
                logging.info ('===================name right===================')
        except:
            logging.error ("====================name error===================")
            return 5
        try:
            if now_protocol == portSection:
                logging.info  ('===================portSection right===================')
        except:
            print ("====================portSection2 error===================")
            return 5
        try:
            if now_ip == (str(full_ip)+str(last_ip)):
                logging.info  ('===================ip right ====================')
        except:
            logging.error ("====================ip error===================")
            return 5
        try:
            if now_outport == str(outport):
                logging.info  ('===================ouport right=================')
        except:
            logging.error ('===================ouport error=================')
            return 5
        try:
            if now_inport == str(inport):
                logging.info  ('===================inport right=================')
        except:
            logging.error ('===================inport error=================')
            return 5
        try:
            if now_state == state:
                logging.info  ('===================state right===================')
        except:
            logging.error ("====================state error===================")
            return 5
        return 1
    #删除规则
    def delete_portforward(self,driver,operation):
        time.sleep(2)
        driver.find_element_by_id("btn_portSection1_del").click()
        time.sleep(1)
        if operation == '确定':
            driver.find_element_by_xpath("//div[@class='newifi-btn btn-sure']").click()
        elif operation == '取消':
            driver.find_element_by_xpath("//div[@class='newifi-btn btn-cancel']").click()
        time.sleep(5)
        return 1
    #检查没有规则的情况
    def check_no_portforward(self,driver):
        time.sleep(2)
        now_list = driver.find_element_by_xpath("//p[text()='尚未添加任何数据']").is_displayed()
        if now_list:
            logging.info (u"================no portforward==============")
            return 1
        else:
            logging.error (u"================have portforward================")
            return 6

#输入异常的DMZ主机IP地址
    def input_illegal_DMZ_ip(self,driver,list=[""]):
        time.sleep(2)
        try:
            for dmz_ip in list:
                time.sleep(2)
                driver.find_element_by_xpath("//input[@class='form-input dmz-input luci2-field-validate']").clear()
                driver.find_element_by_xpath("//input[@class='form-input dmz-input luci2-field-validate']").send_keys(dmz_ip)
                driver.find_element_by_id("dmz_btn").click()
                time.sleep(2)
                msg = driver.find_element_by_xpath(".//*[@id='portdmz_dmz']/div[4]/div[2]/div/div[1]/div/div").text
                if msg == "请输入需要设置为DMZ主机的IP地址!":
                    logging.info("==============input null dmz ip pass==============")
                    print(msg)
                elif msg == "请输入2-254的正整数！":
                    logging.info("====  ==========input illegal dmz ip pass================")
                else:
                    return 0
            return 1
        except Exception as e:
            logging.error(u"=============error: input_illegal_DMZ_ip failed%s================="%e)
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/input_illegal_DMZ_ip-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
    #端口转发异常输入名称
    def input_Abnormal_character_Portforward_usrname(self,driver,Abnormal_character):
        try:
            driver.find_element_by_xpath(".//*[@id='port_addNewEntery']/span").click()
            driver.find_element_by_id("portSection2_port_name").clear()
            driver.find_element_by_id("portSection2_port_name").send_keys(Abnormal_character)
            driver.find_element_by_id("btn_portSection2_save").click()
            time.sleep(1)
            error_msg = driver.find_element_by_xpath(".//*[@id='section-pane-portSection2']/div[1]/div/div").text
            if error_msg == "请输入名称！":
                logging.info("====================input null user name pass===================")
                return 1
            elif error_msg == "请输入1-60个字符的名称！":
                logging.info("====================input over length user name pass===================")
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/input_abnormal_urrname_error-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
    #端口转发异常输入IP地址
    def input_Abnormal_character_Portforward_address(self,driver,Abnormal_character_list = [""]):
        try:
            driver.find_element_by_xpath(".//*[@id='port_addNewEntery']/span").click()
            for Abnormal_character in Abnormal_character_list:
                driver.find_element_by_xpath(".//*[@id='portSection2_port_ip']/input").clear()
                driver.find_element_by_xpath(".//*[@id='portSection2_port_ip']/input").send_keys(Abnormal_character)
                driver.find_element_by_id("btn_portSection2_save").click()
                time.sleep(1)
                error_msg = driver.find_element_by_xpath(".//*[@id='section-pane-portSection2']/div[3]/div/div[2]").text
                if error_msg == "请输入IP地址最后一位！":
                    logging.info("====================input null user name pass===================")
                elif error_msg == "请输入2-254的正整数！":
                    logging.info("====================input over length user name pass===================")
                else:
                    return 0
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/input_abnormal_address_error-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
    #端口转发外部端口异常输入
    def input_Abnormal_outportt(self,driver,out_ip_one_list = [""],out_ip_two_list = [""]):
        try:
            driver.find_element_by_xpath(".//*[@id='port_addNewEntery']/span").click()
            for out_ip_one in out_ip_one_list:
                driver.find_element_by_xpath(".//*[@id='portSection2_port_outside']/input[1]").clear()
                driver.find_element_by_xpath(".//*[@id='portSection2_port_outside']/input[1]").send_keys(out_ip_one)
                for out_ip_two in out_ip_two_list:
                    driver.find_element_by_xpath(".//*[@id='portSection2_port_outside']/input[2]").clear()
                    driver.find_element_by_xpath(".//*[@id='portSection2_port_outside']/input[2]").send_keys(out_ip_two)
                    driver.find_element_by_id("btn_portSection2_save").click()
                    time.sleep(2)
                    out_ip_msg = driver.find_element_by_xpath(".//*[@id='section-pane-portSection2']/div[4]/div/div[2]").text
                    if out_ip_msg == "请输入外部端口！":
                        logging.info("==================outside ip input null warn msg pass==================")
                    elif out_ip_msg == "请输入0-65535的正整数！":
                        logging.info("==================outside ip input abnormal warn msg pass==================")
                    elif out_ip_msg == "请输入合理端口段！":
                        logging.info("==================input Unjustified outside address warn msg pass ==================")
                    else:
                        return 0
            return 1
        except:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/input_abnormal_outsideport-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
    #端口转发内部端口异常输入
    def input_Abnormal_insideport(self,driver,inside_ip_one_list = [""],inside_ip_two_list = [""]):
        try:
            driver.find_element_by_xpath(".//*[@id='port_addNewEntery']/span").click()
            for inside_ip_one in inside_ip_one_list:
                driver.find_element_by_xpath(".//*[@id='portSection2_port_inside']/input[1]").clear()
                driver.find_element_by_xpath(".//*[@id='portSection2_port_inside']/input[1]").send_keys(inside_ip_one)
                for inside_ip_two in inside_ip_two_list:
                    driver.find_element_by_xpath(".//*[@id='portSection2_port_inside']/input[2]").clear()
                    driver.find_element_by_xpath(".//*[@id='portSection2_port_inside']/input[2]").send_keys(inside_ip_two)
                    driver.find_element_by_id("btn_portSection2_save").click()
                    out_ip_msg = driver.find_element_by_xpath(".//*[@id='section-pane-portSection2']/div[4]/div/div[2]").text
                    inside_ip_msg = driver.find_element_by_xpath(".//*[@id='section-pane-portSection2']/div[5]/div/div[2]").text
                    if inside_ip_msg == "请输入内部端口！":
                        logging.info("==================outside ip input null warn msg pass==================")
                    elif inside_ip_msg == "请输入0-65535的正整数！":
                        logging.info("==================outside ip input abnormal warn msg pass==================")
                    elif inside_ip_msg == "请输入合理端口段！":
                        logging.info("==================input Unjustified outside address warn msg pass ==================")
                    else:
                        return 0
            return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/input_abnormal_insideport-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
    #端口转发外部端口号冲突
    def Port_conflict_portforward(self,driver):
        try:
            time.sleep(2)
            status = driver.find_element_by_xpath("//p[text()='外部端口号冲突，请重新设置！']").is_displayed()
            if status:
                logging.info("===================Port_conflict_portforward pass===================")
                return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/Port_conflict_portforward-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0

    #检查无线MAC过滤状态
    def check_macfilter_status(self,driver):
        try:
            driver.find_element_by_xpath("//span[text()='无线MAC过滤']").click()
            time.sleep(3)
            class_value = driver.find_element_by_id("mac_switch").get_attribute("class")
            if class_value == "section-switch dmz-switch  switch-off":
                logging.info("================macfilter is closed================")
                return 1
            elif class_value == "section-switch dmz-switch  switch-on":
                logging.info("================macfilter is open================")
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/check_macfilter_status-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
    #检查mac过滤开启后的页面内容
    def check_macfilter_web(self,driver):
        try:
            driver.find_element_by_xpath("//span[text()='无线MAC过滤']").click()
            time.sleep(2)
            driver.find_element_by_id("mac_switch").click()
            time.sleep(3)
            str_title = driver.find_element_by_xpath("//div[@class='mac-tabs']").text.split()
            str_online = driver.find_element_by_xpath(".//*[@id='online']/table/thead/tr").text.split()
            if str_title[0] == "在线设备" and str_title[1] == "离线设备" and str_title[2] == "黑名单" and str_title[3] == "手动添加":
                if str_online[0] == "设备名称" and str_online[1] == "详情" and str_online[2] == "黑名单配置":
                    if driver.find_element_by_xpath("//div[text()='无法设置']").text == "无法设置":
                        logging.info("==================check_macfilter_web pass=================")
                        return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/check_macfilter_web-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
    # #手动添加mac过滤
    def Manual_addition_macFilter(self,driver,mac_name_list=[""],mac_addr_list=[""]):
        try:
            driver.find_element_by_xpath("//span[text()='无线MAC过滤']").click()
            time.sleep(2)
            driver.find_element_by_id("mac_add").click()
            time.sleep(1)
            for mac_name in mac_name_list:
                driver.find_element_by_id("mac_name").clear()
                driver.find_element_by_id("mac_name").send_keys(mac_name)
                for mac_addr in mac_addr_list:
                    time.sleep(4)
                    if mac_addr != "":
                        driver.find_element_by_id("mac_addr").clear()
                        driver.find_element_by_id("mac_addr").send_keys(mac_addr)
                    elif mac_addr == "":
                        driver.find_element_by_id("mac_addr").clear()
                        driver.find_element_by_id("mac_addr").send_keys(Keys.BACK_SPACE)
                warn_msg_name= driver.find_element_by_xpath(".//*[@id='ma-name']").text
                if warn_msg_name == "设备名称不能为空":
                    logging.info("===================null name pass=================")
                    return 1
                elif warn_msg_name == "设备名称最多可输入27个字符":
                    logging.info("===================over long name pass================")
                    return 2
                warn_msg_mac = driver.find_element_by_id("ma-mac").text
                print(warn_msg_mac)
                if warn_msg_mac == "MAC地址不能为空":
                    logging.info("=================null mac address pass====================")
                    return 3
                elif warn_msg_mac == "请输入正确的MAC地址,如:00:1D:0F:11:22:33":
                    logging.info("=================abnormal mac input pass====================")
                    return 4
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/Manual_addition_macFilter-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0
    #手动设置一个MAC过滤地址，并移除
    def save_and_delete_macfilter(self,driver,mac_name,mac_addr):
        try:
            driver.find_element_by_xpath("//span[text()='无线MAC过滤']").click()
            time.sleep(2)
            driver.find_element_by_id("mac_add").click()
            time.sleep(1)
            driver.find_element_by_id("mac_name").clear()
            driver.find_element_by_id("mac_name").send_keys(mac_name)
            driver.find_element_by_id("mac_addr").clear()
            driver.find_element_by_id("mac_addr").send_keys(mac_addr)
            driver.find_element_by_id("btn_raw0").click()
            time.sleep(4)
            driver.find_element_by_xpath(".//*[@id='c']/a").click()
            time.sleep(2)
            str_list = driver.find_element_by_id("backlist-tbody").text.split()
            if str_list[0] == "test" and str_list[1] == "MAC地址00:1d:0f:11:22:33":
                driver.find_element_by_xpath(".//*[@id='backlist-tbody']/tr/td[3]/div").click()
                time.sleep(4)
                try:
                    driver.find_element_by_id("backlist-tbody").is_displayed()
                except Exception as e:
                    print(e)
                    return 1
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd())+"/errorpng/save_and_delete_macfilter-%s.jpg" % time.strftime("%Y%m%d%H%M%S", time.localtime()))
            return 0