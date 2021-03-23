from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dato import *
import time
import json
import re
from Facebook_Scraper_POST import Facebook_Scraper_POST


if __name__ == "__main__":
    
    #PATH ="C:/Users/fhaos/Documents/FCQI/8mo/ayundantia/chromedriver.exe"
    PATH = "chromedriver.exe"
    h = Facebook_Scraper_POST(PATH)
    h.loginSession(URL=URL_LOGIN,user=user,password=password)
    h.get(URL_GROUP)
    h.collectionPOST_URL_and_POST_ID(URL_GROUP,10)
    h.Collection_Text_POST(10)
    h.generateJson('post.json')
    
    with open('post.json',encoding='utf-8') as f:
        data_json = json.loads(f.read())
    print(str(data_json[0]['post_ID']))
    
    print('\n *** visitas *** \n')
    h.test_User_names(data_json[0]['post_ID'],URL_VISITED,"people_visited.json","visited_names")

    h.test_User_names(data_json[0]['post_ID'],URL_LIKED,"people_liked.json","liked_names")
    # print('\n *** likes *** \n')
    # h.test_User_liked(data_json[0]['post_ID'])
    # print('\n *** compartidas *** \n')
    # h.test_User_shared(data_json[0]['post_ID'])
    
    
    