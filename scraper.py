from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dato import user,password
import time
import json
import re
from Facebook_Scraper_POST import Facebook_Scraper_POST


if __name__ == "__main__":
    
    PATH ="C:/Users/fhaos/Documents/FCQI/8mo/ayundantia/chromedriver.exe"
    h = Facebook_Scraper_POST(PATH)
    h.loginSession(URL="https://mbasic.facebook.com/",user=user,password=password)
    h.get("https://m.facebook.com/groups/413938496303058")
    h.collectionPOST_URL_and_POST_ID("https://m.facebook.com/groups/413938496303058",10)
    h.Collection_Text_POST(10)
    h.generateJson('post.json')
