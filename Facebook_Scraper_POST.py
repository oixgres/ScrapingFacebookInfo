
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from element_html import *
import time
import re
import json
class Facebook_Scraper_POST:

    POST_URL =[]
    POST_ID =[]
    POSTER_NAME =[]
    USER_ID = []
    POSTER_TEXT=[]



    def __init__(self,path):
        self.driver = webdriver.Chrome(path)

    def get(self,URL):
        self.driver.get(URL)


    
    def loginSession(self,URL,user ,password):  
        self.driver.get(URL)                                                        # acceder page-login
        self.driver.find_element_by_id(LOGIN_EMAIL_ID).send_keys(user)             # introduce usuario
        self.driver.find_element_by_name(PASSWORD_NAME).send_keys(password)                # introduce password
        self.driver.find_element_by_name(PASSWORD_NAME).send_keys(Keys.RETURN)             # enter
        time.sleep(3)
        iniciar_seccion_no_toque = self.driver.find_element_by_xpath(INPUT_NO_TOUCH_XPATH)
        iniciar_seccion_no_toque.click()


    def collectionPOST_URL_and_POST_ID(self,URL,number_POST):
        index=0
        self.driver.get(URL)                                                 # acceder la pagina del grupo
        self.scroll_max()                                                    # mostrar todas las publicaciones
        
        links = self.driver.find_elements_by_xpath(ARTICLE_LINK_XPATH)    # Encontrar todos elementos article(enlace de la publicacion)
       
        if len(links)>=number_POST:                                          # Obtener los post basando en el number_POST
            for link in range(number_POST):
                js_script="return document.getElementsByTagName('article')["+str(index)+"].dataset.store"
                self.POST_URL.append(str(links[link].get_attribute('href').split('?')[0]))
                data_post = self.driver.execute_script(js_script)
                self.POST_ID.append(re.findall(r"top_level_post_id.(.+?):",str(data_post))[0])
                print(self.POST_ID[index])
                index+=1
                
        else:
            index=0
            for link in links:
                js_script="return document.getElementsByTagName('article')["+str(index)+"].dataset.store"
                self.POST_URL.append(str(link.get_attribute('href').split('?')[0]))
                data_post = self.driver.execute_script(js_script)
                self.POST_ID.append(re.findall(r"top_level_post_id.(.+?):",str(data_post))[0])
                index+=1
                

        

    def Collection_Text_POST(self,number_POST):
        if number_POST>len(self.POST_URL):
            number_POST=len(self.POST_URL)
        for index in range(number_POST):
            self.driver.get(self.POST_URL[index])
            poster_text=self.driver.find_element_by_xpath(POST_TEXT_XPATH)
            poster_name=self.driver.find_element_by_xpath(POSTER_NAME_XPATH)
            self.POSTER_NAME.append(poster_name.text)
            self.POSTER_TEXT.append(poster_text.text)

    def generateJson (self,file):
        file = open(file,'w+',encoding="utf-8")
        data=[]
        

        for index in range(len(self.POST_URL)):
            element={}
            element["link"]=self.POST_URL[index]
            element["poster_name"]=self.POSTER_NAME[index]
            element["post_ID"]=self.POST_ID[index]
            element["post_text"]=self.POSTER_TEXT[index]
            data.append(element)
                  
        json.dump(data,file,indent=4, ensure_ascii=False)
        file.close()
        
    #https://m.facebook.com/ufi/group/seenby/profile/browser/?id=433655667664674
    #Obtener usuarios que visitaron el post

    # @parameter POST_ID int
    # @parameter file string
    # @parameter type_user string visited_name shared_name liked_name

    def test_User_names(self,POST_ID,URL_type,file,type_names):
        URL=URL_type+str(POST_ID)
        self.driver.get(URL)
        
        t=True
        json_data={} 
        json_data["link_ID"]=POST_ID
        while t:
            try:
                self.driver.find_element_by_xpath(BOTTOM_SEE_MORE_XPATH).click()   # clic al elemento ver mas
                time.sleep(1)
            except NoSuchElementException:  
                t=False
                pass
        list_name = self.driver.find_elements_by_xpath(LIST_NAME_XPATH)
        visited_names=[]
        
        index = 1
        for name in list_name:
            if len(name.text)>0:
                visited_name={}
                key='name'+str(index)
                visited_name[key]=name.text
                visited_names.append(visited_name)
                index+=1
                print(name.text)
        json_data["number"]=len(visited_names)
        json_data[type_names]=visited_names
        file = open(file,'w+',encoding="utf-8")
        json.dump(json_data,file,indent=4, ensure_ascii=False)
        file.close()
        
    
    
    def scroll_max(self):
        t = True
        while t:
            scrollHeight_now = self.driver.execute_script("return document.body.scrollHeight;")

            for r in range(10):
                self.driver.execute_script("window.scrollBy(0,1500)")
            time.sleep(2)
            scrollHeight_scrolled=self.driver.execute_script("return document.body.scrollHeight;")
            if scrollHeight_scrolled==scrollHeight_now:
                t=False



    # https://m.facebook.com/story.php?story_fbid=2765539700363999&id=1629107234007257&anchor_composer=false
    def test_comment_POST(self,URL):
        self.scroll_to_max_height_comment(URL)
        self.see_comments_secondary(SEE_COMMENTS_SECONDARY_CLASS_NAME)
        boxs = self.driver.find_elements_by_xpath("//div[@class='_2b04']") 
        json_post_comments={}
        comments =[]
        num_comment = 0
        for box in boxs:
            try:
                name = box.find_element_by_css_selector(" div._2b06 > div._2b05")
                comment_Text = box.find_element_by_css_selector(" div._2b06 > div:nth-child(2)")
                comment={}
                num_comment+=1
                comment['number_comment']=num_comment
                comment['name']=name.text
                comment['comment_text']=comment_Text.text
                comments.append(comment)
            except NoSuchElementException:
                print("usuario no capturado por uso de gif")
                pass
        #json_post_comment['post_id']=post_id
        json_post_comments['total_comments']=num_comment
        json_post_comments['comments']=comments
        file = open('post_comments.json','w+',encoding="utf-8")
        json.dump(json_post_comments,file,indent=4, ensure_ascii=False)
        file.close()
        

    
    def see_comments_secondary(self,class_name):
        for bton in self.driver.find_elements_by_class_name(class_name):
                    bton.click()
                    time.sleep(0.5)


    def see_past_comment(self,web_elements):
        for web_element in web_elements:
            t=True
            while t:
                try:
                    web_element.find_element_by_xpath('//a[@class="async_elem"]').click()   # clic al elemento ver mas
                    time.sleep(1)
                except NoSuchElementException:  
                    t=False
                    pass


    def scroll_to_max_height_comment(self,URL):
        self.driver.get(URL)
        t=True
        while t:
            try:
                self.driver.find_element_by_xpath('//div[@class="async_elem"]').click()   # clic al elemento ver mas
                time.sleep(2)
            except NoSuchElementException:  
                t=False
                pass
        



    