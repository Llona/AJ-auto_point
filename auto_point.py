from selenium import webdriver
from time import sleep
import sys
import settings
from datetime import datetime
import random
import os


class WebDriverControl(object):
    def __init__(self):
        super(WebDriverControl, self).__init__()
        self.username = ''
        self.password = ''

    @staticmethod
    def create_driver(option):
        if sys.platform.startswith('win'):
            driver = webdriver.Chrome(settings.WEB_DRIVER_PATH_WIN, options=option)
        else:
            driver = webdriver.Chrome(settings.WEB_DRIVER_PATH_LINUX, chrome_options=option)

        # driver.implicitly_wait(10)
        return driver

    def init_driver(self):
        option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        # option.add_argument("--start-maximized")
        return self.create_driver(option)

    def init_driver_headless(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument("window-size=1920,1080")
        # option.add_argument("--start-maximized")
        return self.create_driver(option)


class AutoPoint(WebDriverControl):
    def __init__(self):
        super(AutoPoint, self).__init__()

        self.isoweek = datetime.today().isoweekday()

        driver_control = WebDriverControl()

        if settings.DEBUG:
            self.driver = driver_control.init_driver()
        else:
            self.driver = driver_control.init_driver_headless()

    def start(self):
        if self.isoweek > 5:
            # do not run when week 6 and 7
            self.log_print("no need to run, return!!")
            self.stop()
            return

        self.log_print("start!")

        if settings.RANDOM_DELAY:
            delay_time = random.randint(0, settings.RANDOM_DELAY_SECOND)
            print_str = "random delay : " + str(delay_time) + " second"
            print(print_str)
            self.log_print(print_str)

            sleep(delay_time)

        try:
            self.driver.get(settings.POINT_URL)
            element = self.driver.find_element_by_class_name("checkHealth")
            element.click()
            sleep(2)
            element = self.driver.find_element_by_name("send")
            element.click()
            sleep(2)

            self.log_print("success!")
        except Exception as e:
            self.log_print("error!, log: " + str(e))
        finally:
            self.stop()

    def stop(self):
        self.driver.quit()
        self.log_print("*************", data_time=False)

    def log_print(self, log_str, data_time=True):
        today_str = str(datetime.today())
        isoweek_str = str(self.isoweek)
        if data_time:
            log_str = "echo " + today_str + " week: " + isoweek_str + " , " + log_str + " >> " + settings.LOG_PATH
        else:
            log_str = "echo " + log_str + " >> " + settings.LOG_PATH
        os.system(log_str)


auto_control = AutoPoint()
auto_control.start()
