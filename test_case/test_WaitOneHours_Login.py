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
    default_pw=config.get("Default",'default_pw')
    fail_pw = config.get('Default', 'fail_pw')
    logging.info(__file__)
    conftest.browser()
    driver = conftest.driver
    driver.maximize_window()
    if lr.open_url(driver,'http://'+default_ip)==1:
        for i in range(10):
            logging.info("=== Login password === %s " % fail_pw)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(fail_pw)
            time.sleep(2)
            driver.find_element_by_css_selector('#sysauth > div > div > div.login-modal-content > div.modal-footer.login-modal-footer > div').click()
        try:
            logging.info("wait one hours to Login")
            time.sleep(3600)
            if lr.login(driver,default_pw)==1:
                return 1
            else:
                logging.info("Fail!!!!!!!!!")
                return 2
        except Exception as e:
            driver.get_screenshot_as_file(os.path.dirname(os.getcwd()) + "/errorpng/loginfail-%s.jpg" % ctime())
            logging.error("===LOgin ERROR ===%s" % e)
            return 0
        finally:
            pass
    driver.quit()

def test_continue_logindail():
    assert case()==1

if __name__ == '__main__':
    pytest.main(os.path.basename(__file__))