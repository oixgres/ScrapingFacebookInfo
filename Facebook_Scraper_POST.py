
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from element_html import *
from dato import *
import time
import re
import json
class Facebook_Scraper_POST:

    def __init__(self,path):
        self.driver = webdriver.Chrome(path)

    def get(self,URL):
        self.driver.get(URL)

    def loginSession(self,URL,user ,password):
        self.driver.get(URL) # acceder page-login
        self.driver.find_element_by_id(LOGIN_EMAIL_ID).send_keys(user) # introduce usuario
        self.driver.find_element_by_name(PASSWORD_NAME).send_keys(password) # introduce password
        self.driver.find_element_by_name(PASSWORD_NAME).send_keys(Keys.RETURN) # enter
        time.sleep(3)
        iniciar_seccion_no_toque = self.driver.find_element_by_xpath(INPUT_NO_TOUCH_XPATH)
        iniciar_seccion_no_toque.click()


    def collectionPOST(self,URL,number_POST):

        POST_URL =[]
        POST_ID =[]
        POSTER_NAME =[]
        POSTER_TEXT=[]

        index=0
        self.driver.get(URL)  # acceder la pagina del grupo
        self.controlled_scroll(number_POST) # mostrar todas las publicaciones

        links = self.driver.find_elements_by_xpath(ARTICLE_LINK_XPATH) # Encontrar todos elementos article(enlace de la publicacion)

        if number_POST>len(links):
            number_POST=len(links)-2 
        
        # Obtener los post basando en el number_POST
        for link in range(number_POST):
            print(index)
            js_script="return document.getElementsByTagName('article')["+str(index)+"].dataset.store"
            data_post = self.driver.execute_script(js_script)
            POST_ID.append(re.findall(r"top_level_post_id.(.+?):",str(data_post))[0])
            POST_URL.append(URL_POST_LINK+str(POST_ID[index]))
            index+=1
        
        for index in range(number_POST):
            self.driver.get(POST_URL[index])
            print(index)
            try:
                poster_text=self.driver.find_element_by_xpath(POST_TEXT_XPATH)
                POSTER_TEXT.append(poster_text.text)
            except NoSuchElementException:
                POSTER_TEXT.append("No hay texto")
            try:
                poster_name=self.driver.find_element_by_xpath(POSTER_NAME_XPATH)
                POSTER_NAME.append(poster_name.text)
            except NoSuchElementException:
                POSTER_NAME.append("desconoce el nombre")

            time.sleep(2)
        print(len(POST_URL))
        data=[]
        for index in range(len(POST_URL)):
            element={}
            element['id_post']=POST_ID[index]
            element['id_grupo']=URL[URL.rfind("/")+1:]
            element['url']=POST_URL[index] 
            element['user']=POSTER_NAME[index]
            element['text']=POSTER_TEXT[index]
            data.append(element)

        return data


    #Obtener usuarios que visitaron el post

    # @parameter POST_ID int
    # @parameter file string
    # @parameter type_user string visited_name shared_name liked_name
    def getUsernames(self,POST_ID,URL_type,type_names):
        url=URL_type+str(POST_ID)
        self.driver.get(url)

        t=True

        while t:
            try:
                self.driver.find_element_by_xpath(BOTTOM_SEE_MORE_XPATH).click()   # clic al elemento ver mas
                time.sleep(3)
            except NoSuchElementException:
                t=False
                pass
        list_name = self.driver.find_elements_by_xpath(LIST_NAME_XPATH)
        total_names=[]
        json_data={}
        json_data['idPost']=POST_ID
        index = 1
        for name in list_name:
            if len(name.text)>0:
                user={}
                user['idPost']= POST_ID
                user['persona']=name.text
                
                
                total_names.append(user)
                #print(name.text)
                
        json_data[type_names]=total_names
        return json_data

    def get_reactions(self, POST_ID, URL_type):
        url = URL_type+str(POST_ID)
        self.driver.get(url)
        
        #Arreglo con los resultados de la busqueda
        result = []

        #Creamos una copia por que los cortaremos y no queremos perder los datos
        allReactionsIDArray = ALL_REACTIONS_ID.copy()
        allReactionsXPathArray = ALL_REACTIONS_XPATH.copy()
        allReactionsNameArray = ALL_REACTIONS_NAME.copy()


        #Damos click de reaccion en reaccion
        for button in self.driver.find_elements_by_xpath(REACTION_BUTTON_XPATH):
            button.click()
            time.sleep(1)
            index = 0
            
            #Identificamos cual reaccion es a la que le dimos click
            for path in allReactionsXPathArray:
                reactionGroup = {}
                #Verificamos que exista la reaccion
                if self.driver.find_elements_by_id(allReactionsIDArray[index]):
                    #Verificamos que este desplegada la info de la reaccion
                    if self.driver.find_elements_by_xpath(allReactionsXPathArray[index]):
                        list_name = self.driver.find_elements_by_xpath(allReactionsXPathArray[index])

                        reactions= []

                        #Transformamos los nombres de quienes reaccionaron a texto
                        for name in list_name:
                            if len(name.text) > 0:
                                #Contenido de una reaccion
                                data={}
                                data['idPost'] = POST_ID
                                data['tipo'] = allReactionsNameArray[index]
                                data['persona'] = name.text
                                reactions.append(data)
                                
                        #Las reacciones de un mismo tipo se almacenan en grupos
                        reactionGroup['type'] = allReactionsNameArray[index]
                        reactionGroup['reactions'] = reactions
                        result.append(reactionGroup)

                        #Quitamos lo ya encontrado para no repetir busquedas
                        allReactionsXPathArray.pop(index)
                        allReactionsNameArray.pop(index)
                        allReactionsIDArray.pop(index)
                        break;

                index+=1
        return result


    def controlled_scroll(self, times):
        for i in range(times):
            scrollHeight_now = self.driver.execute_script("return document.body.scrollHeight;")
        
            for r in range(10):
                self.driver.execute_script("window.scrollBy(0,1500)")
                
            time.sleep(3)
            scrollHeight_scrolled=self.driver.execute_script("return document.body.scrollHeight;")
            if scrollHeight_scrolled==scrollHeight_now:
                break
                
    def scroll_max(self):
        t = True
        while t:
            scrollHeight_now = self.driver.execute_script("return document.body.scrollHeight;")

            for r in range(10):
                self.driver.execute_script("window.scrollBy(0,1500)")
            time.sleep(3)
            scrollHeight_scrolled=self.driver.execute_script("return document.body.scrollHeight;")
            if scrollHeight_scrolled==scrollHeight_now:
                t=False

    def getComments(self, url, postId):
    
        postUrl= url+'/'+str(postId)
        self.driver.get(url)
        self.see_comments_secondary(SEE_COMMENTS_SECONDARY_CLASS_NAME)

        #Caja de comentarios
        box = self.driver.find_elements_by_xpath(COMMENT_BOX)
        names = self.driver.find_elements_by_xpath(NAMES_COMMENT)
        result =[]
        
        if box:
            for comment in box:
                #Comentarios principales
                main = comment.find_elements_by_xpath(MAIN_COMMENT)
                comments={}
                primaryComment={}
                secondaryComments=[]
                
                if names == []:
                    break; 

                if main:
                    to=self.getToName(main[0])
                    idComment=self.getIdComment(main[0])
                    primaryComment['idPost']=postId
                    primaryComment['idComment']=idComment
                    primaryComment['name']=main[0].find_element_by_xpath(NAMES_COMMENT_ALT).text
                    primaryComment['content']=main[0].text
                    primaryComment['to']=to
                else:
                    main = comment.find_elements_by_xpath(MAIN_COMMENT_GIF)
                    primaryComment['idPost']=postId
                    primaryComment['idComment']=idComment+'G'
                    primaryComment['name']=main[0].find_element_by_xpath(NAMES_COMMENT_ALT).text
                    primaryComment['content']="IMAGEN-GIF "
                    primaryComment['to']=''

                names.pop(0)

                #Respuestas
                answers = comment.find_elements_by_xpath(SEC_COMMENT)
                if answers:
                    for answer in answers:
                        secondaryComment={}
                        to=self.getToName(answer)
                        secondaryIdComment=self.getIdComment(answer)
                        secondaryComment['postId']=postId
                        secondaryComment['fromId']=secondaryIdComment
                        secondaryComment['name']=answer.find_element_by_xpath(NAMES_COMMENT_ALT).text
                        secondaryComment['content']=answer.text
                        secondaryComment['toId']=idComment
                        secondaryComment['toName']=to
                        secondaryComments.append(secondaryComment)
                        names.pop(0)
                else:
                    answers = comment.find_elements_by_xpath(SEC_COMMENT_GIF)
                    if answers:
                        for answer in answers:
                            secondaryComment={}
                            to=self.getToName(answer)
                            secondaryIdComment=self.getIdComment(answer)
                            secondaryComment['postId']=postId
                            secondaryComment['fromId']=secondaryIdComment
                            secondaryComment['name']=answer.find_element_by_xpath(NAMES_COMMENT_ALT).text
                            secondaryComment['content']=answer.text
                            secondaryComment['toId']=idComment
                            secondaryComment['toName']=to
                            secondaryComments.append(secondaryComment)
                            names.pop(0)
                    else:
                        answers = comment.find_elements_by_xpath(TRADUCT_COMMENT)
                        for answer in answers:
                            secondaryComment={}
                            to=self.getToName(answer)
                            secondaryIdComment=self.getIdComment(answer)
                            secondaryComment['postId']=postId
                            secondaryComment['fromId']=secondaryIdComment
                            secondaryComment['name']=answer.find_element_by_xpath(NAMES_COMMENT_ALT).text
                            secondaryComment['content']=answer.text
                            secondaryComment['toId']=idComment
                            secondaryComment['toName']=to
                            secondaryComments.append(secondaryComment)
                            names.pop(0)
                        else:
                            answers = comment.find_elements_by_xpath(SEC_COMMENT_GIF_AND_TEXT)
                            for answer in answers:
                                secondaryComment={}
                                to=self.getToName(answer)
                                secondaryIdComment=self.getIdComment(answer)
                                secondaryComment['postId']=postId
                                secondaryComment['fromId']=secondaryIdComment
                                secondaryComment['name']=answer.find_element_by_xpath(NAMES_COMMENT_ALT).text
                                secondaryComment['content']=answer.text
                                secondaryComment['toId']=idComment
                                secondaryComment['toName']=to
                                secondaryComments.append(secondaryComment)
                                names.pop(0)
                comments['primaryComment']=primaryComment
                comments['secondaryComment']=secondaryComments
                result.append(comments)

        return result
                    

    def getIdComment (self,webElement):
        idComment=webElement.get_attribute('data-commentid')
        return idComment[str(idComment).find('_')+1:]

    def getToName(self,webElement):
        name=''
        try :
            name=webElement.find_element_by_css_selector('a').text
        except  NoSuchElementException:
            pass
        return name
     
    #Da click a todos los comentarios secundarios
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

    def scroll_to_max_height_comment(self):
        t=True
        while t:
            try:
                self.driver.find_element_by_xpath('//div[@class="async_elem"]').click()   # clic al elemento ver mas
                time.sleep(3)
            except NoSuchElementException:
                t=False
                pass
