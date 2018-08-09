import time,logging
import base64
from appium import webdriver

class install_APP:
    def install_app(self, driver, app_path):
        time.sleep(2)
        try:
            driver.install_app(app_path)
            return 1
        except Exception as e:
            return 0

    def uninstall_app(self, driver):
        time.sleep(2)
        try:
            driver.remove_app("com.diting.newifi.bridge")
            return 1
        except Exception as e:
            return 0

    def push_app(self, driver):
        time.sleep(2)
        try:
            app_path = open("C:\\newifi_v3.4.1.2.apk")
            app_data = app_path.read()
            base64_data = base64.b64encode(app_data)
            driver.push_file("/storage/sdcard0/Download/", base64_data)
            return 1
        except Exception as e:
            return 0

