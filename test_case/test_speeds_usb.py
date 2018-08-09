# -*- coding: utf-8 -*-
import configparser
import logging
import time
import os
import pytest
#########################
#  import module
#########################
import sys
import conftest
sys.path.append("..")
import modules.login_router
import modules.router_setup
import modules.initialize
import modules.device_management
from modules.login_router import *
from modules.router_setup import *
from modules.wifi import *
from tools import *
from test_case.test_speeds import *
from test_case.test_checkusb import *
#########################
from selenium import webdriver

for i in range(1,20):
    os.system('py.test test_speeds.py test_checkusb.py')
