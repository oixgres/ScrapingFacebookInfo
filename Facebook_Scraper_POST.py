
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        self.driver.find_element_by_id("m_login_email").send_keys(user)             # introduce usuario
        self.driver.find_element_by_name("pass").send_keys(password)                # introduce password
        self.driver.find_element_by_name("pass").send_keys(Keys.RETURN)             # enter
        time.sleep(3)
        iniciar_seccion_no_toque = self.driver.find_element_by_xpath("//div/input")
        iniciar_seccion_no_toque.click()


    def collectionPOST_URL_and_POST_ID(self,URL,number_POST):
        index=0
        self.driver.get(URL)                                                 # acceder la pagina del grupo
        self.scroll_max()                                                    # mostrar todas las publicaciones
        
        links = self.driver.find_elements_by_xpath("//a[@class='_5msj']")    # Encontrar todos elementos article(enlace de la publicacion)
       
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
            texto=self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[1]/div[1]/div/div/div[1]/div[1]/div")
            user_name=self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[1]/div[1]/div/div/div[1]/header/div[2]/div/div/div[1]/h3/span/strong[1]/a")
            self.POSTER_NAME.append(user_name.text)
            self.POSTER_TEXT.append(texto.text)

    def generateJson (self,file):
        file = open(file,'w+',encoding="utf-8")
        json_element={
        "link":"",
        "poster_name":"",
        "post_ID":0,
        "post_text":""
        }

        for index in range(len(self.POST_URL)):
            json_element["link"]=self.POST_URL[index]
            json_element["poster_name"]=self.POSTER_NAME[index]
            json_element["post_ID"]=self.POST_ID[index]
            json_element["post_text"]=self.POSTER_TEXT[index]            
            json.dump(json_element,file,indent=4, ensure_ascii=False)
            
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

    