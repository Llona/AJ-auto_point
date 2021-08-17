# -*- coding: utf-8 -*-
import sys
import os

DEBUG = False
RANDOM_DELAY = True
RANDOM_DELAY_SECOND = 600
POINT_URL = r'http://tpewww/Clock_On/Web/index.aspx'

WEB_DRIVER_PATH_WIN = os.path.join(sys.path[0], "chromedriver.exe")
WEB_DRIVER_PATH_LINUX = '/usr/lib/chromium-browser/chromedriver'

LOG_PATH = os.path.join(sys.path[0], "log.txt")
