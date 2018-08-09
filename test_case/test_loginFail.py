import sys
import conftest
sys.path.append("..")

import modules.login_router
import modules.router_setup
import modules.initialize
import modules.advanced_setup
from modules.login_router import *
from modules.router_setup import *
from modules.initialize import *
from modules.advanced_setup import *
from tools import *
#########################
from selenium import webdriver
def case():
    lr = login_router()
    t=tools()
    projectpath = os.path.dirname(os.getcwd())
    config_file = projectpath + '/configure/' + 'testconfig.ini'
    filename = os.path.basename(__file__).split('.')[0]
    t.log(filename)
    config = configparser.ConfigParser()
    config.read(config_file, encoding='UTF-8')
    default_ip = config.get('Default', 'default_ip')
    fail_pw = config.get('Default', 'fail_pw')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    driver.maximize_window()
    if lr.open_url(driver,'http://'+default_ip)==1:
        try:
            logging.info("=== Login password === %s " % fail_pw)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(fail_pw)
            time.sleep(1)
            logging.info('click login btn')
            driver.find_element_by_css_selector("#sysauth > div > div > div.login-modal-content > div.modal-footer.login-modal-footer > div").click()
            time.sleep(5)
            getRe=driver.find_element_by_css_selector("#sysauth > div > div > div.login-modal-content > div.modal-body.login-modal-body > form > div.login-warn > p").text
            logging.info("get Relay = %s" % getRe)
            print(getRe)
            if getRe=="输入密码错误，请重试！":
                driver.quit()
                return 1
            else:
                return 2
        finally:
            pass

def test_loginfail():
    assert case()==1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))