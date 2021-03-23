from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dato import user,password
import time
import json
import re
from Facebook_Scraper_POST import Facebook_Scraper_POST


if __name__ == "__main__":
    
    #PATH ="C:/Users/fhaos/Documents/FCQI/8mo/ayundantia/chromedriver.exe"
    PATH = "chromedriver.exe"
    h = Facebook_Scraper_POST(PATH)
    h.loginSession(URL="https://mbasic.facebook.com/",user=user,password=password)
    # h.get("https://m.facebook.com/groups/413938496303058")
    # h.collectionPOST_URL_and_POST_ID("https://m.facebook.com/groups/413938496303058",10)
    # h.Collection_Text_POST(10)
    # h.generateJson('post.json')
    
    with open('post.json',encoding='utf-8') as f:
        data_json = json.loads(f.read())
    print(str(data_json[0]['post_ID']))
    
    print('\n *** visitas *** \n')
    h.test_User_visited(data_json[0]['post_ID'])
    print('\n *** likes *** \n')
    h.test_User_liked(data_json[0]['post_ID'])
    print('\n *** compartidas *** \n')
    h.test_User_shared(data_json[0]['post_ID'])
    
    
    