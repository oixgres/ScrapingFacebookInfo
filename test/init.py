import sys 
sys.path.append("..") 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dato import *
import time
import json
import re
from Facebook_Scraper_POST import Facebook_Scraper_POST
from managerFile import readJson,writeJson

PATH = "../chromedriver.exe"
h = Facebook_Scraper_POST(PATH)
h.loginSession(URL=URL_LOGIN,user=user[0],password=password[0])