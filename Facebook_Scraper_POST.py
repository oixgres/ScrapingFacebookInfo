
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
        self.driver.get(URL)                                                        # acceder page-login
        self.driver.find_element_by_id(LOGIN_EMAIL_ID).send_keys(user)             # introduce usuario
        self.driver.find_element_by_name(PASSWORD_NAME).send_keys(password)                # introduce password
        self.driver.find_element_by_name(PASSWORD_NAME).send_keys(Keys.RETURN)             # enter
        time.sleep(3)
        iniciar_seccion_no_toque = self.driver.find_element_by_xpath(INPUT_NO_TOUCH_XPATH)
        iniciar_seccion_no_toque.click()


    def collectionPOST(self,URL,number_POST):

        POST_URL =[]
        POST_ID =[]
        POSTER_NAME =[]
        POSTER_TEXT=[]

        index=0
        self.driver.get(URL)                                                 # acceder la pagina del grupo
        self.scroll_max()                                                    # mostrar todas las publicaciones

        links = self.driver.find_elements_by_xpath(ARTICLE_LINK_XPATH)    # Encontrar todos elementos article(enlace de la publicacion)

        if number_POST>len(links):
            number_POST=len(links)                                      # Obtener los post basando en el number_POST
        for link in range(number_POST):
            js_script="return document.getElementsByTagName('article')["+str(index)+"].dataset.store"

            data_post = self.driver.execute_script(js_script)
            POST_ID.append(re.findall(r"top_level_post_id.(.+?):",str(data_post))[0])
            POST_URL.append(URL_POST_LINK+str(POST_ID[index]))
            print(POST_ID[index])

            index+=1
        for index in range(number_POST):
            self.driver.get(POST_URL[index])
            print("Buscando: "+POST_URL[index])
            try:
                poster_text=self.driver.find_element_by_xpath(POST_TEXT_XPATH)
                POSTER_TEXT.append(poster_text.text)
            except NoSuchElementException:
                POSTER_TEXT.append("No hay texto")
            try:
                poster_name=self.driver.find_element_by_xpath(POSTER_NAME_XPATH)
                POSTER_NAME.append(poster_name.text)
            except NoSuchElementException:
                print("ERROR")

            time.sleep(1)

        data=[]
        for index in range(len(POST_URL)):
            element={}
            element["link"]=POST_URL[index]
            element["poster_name"]=POSTER_NAME[index]
            element["post_id"]=POST_ID[index]
            element["post_text"]=POSTER_TEXT[index]
            data.append(element)

        return data


    #https://m.facebook.com/ufi/group/seenby/profile/browser/?id=433655667664674
    #Obtener usuarios que visitaron el post

    # @parameter POST_ID int
    # @parameter file string
    # @parameter type_user string visited_name shared_name liked_name

    def test_User_names(self,POST_ID,URL_type,type_names):
        url=URL_type+str(POST_ID)
        self.driver.get(url)

        t=True

        while t:
            try:
                self.driver.find_element_by_xpath(BOTTOM_SEE_MORE_XPATH).click()   # clic al elemento ver mas
                time.sleep(2)
            except NoSuchElementException:
                t=False
                pass
        list_name = self.driver.find_elements_by_xpath(LIST_NAME_XPATH)
        visited_names=[]
        json_data={}
        json_data["link_id"]=POST_ID
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
        return json_data

    def get_reactions(self, POST_ID, URL_type):
        url = URL_type+str(POST_ID)
        self.driver.get(url)

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
                username=[]
                data={}
                #Verificamos que exista la reaccion
                if self.driver.find_elements_by_id(allReactionsIDArray[index]):
                    #Verificamos que este desplegada la info de la reaccion
                    if self.driver.find_elements_by_xpath(allReactionsXPathArray[index]):
                        reaction_names = []
                        reaction_names.append(allReactionsNameArray[index])
                        data['reaction']=allReactionsNameArray[index]
                        list_name = self.driver.find_elements_by_xpath(allReactionsXPathArray[index])

                        #Transformamos los nombres de quienes reaccionaron a texto
                        for name in list_name:
                            if len(name.text) > 0:
                                reaction_names.append(name.text)
                                username.append(name.text)
                        #result.append(reaction_names)

                        #Quitamos lo ya encontrado para no repetir busquedas
                        allReactionsXPathArray.pop(index)
                        allReactionsNameArray.pop(index)
                        allReactionsIDArray.pop(index)
                        
                        data['name']=username
                        result.append(data)
                        break;

                index+=1
        return result



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
    def test_comment_POST(self,post_id):
        url=URL_POST_LINK+str(post_id)
        self.driver.get(url)
        self.scroll_to_max_height_comment()
        self.see_comments_secondary(SEE_COMMENTS_SECONDARY_CLASS_NAME)
        boxs = self.driver.find_elements_by_xpath("//div[@class='_2b04']")
        json_post_comments={}
        comments =[]
        num_comment = 0
        for box in boxs:
            try:
                name = box.find_element_by_css_selector(" div._2b06 > div._2b05")    # nombre de usuario de comentario class=_2b05
                comment_Text = box.find_element_by_css_selector(" div._2b06 > div:nth-child(2)") # div:nth-child(2) texto de comentario
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
        json_post_comments['post_Id']=post_id
        json_post_comments['total_comments']=num_comment
        json_post_comments['comments']=comments
        return json_post_comments



        # full_comments_boxs=self.driver.find_elements_by_css_selector('div._2a_i> div._2b04')
        # for full_comments_box in full_comments_boxs:
        #     first_commenter= full_comments_box.find_element_by_css_selector(' div._2b06 >div')                                    # obtener la primera informacion de primer comentarios
        #     first_comment=full_comments_box.find_element_by_css_selector('div._2b06 >div:nth-child(2)')
        #     first_etiqueta=full_comments_box.find_element_by_css_selector('div._2b06 >div:nth-child(2)>a')
        #     print('--------comentario primario--------')
        #     print("name:"+str(first_commenter.text))
        # #   print("to:"+str(first_etiqueta.text))
        #     print("comment:"+str(first_comment.text))
        #     print(str(first_comment.get_attribute('data-commentid')))

    def getComments(self, url):
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
                    
                    print(names[0].text+":")
                    to=self.getToName(main[0])
                    if to : positionName=len(to)+1
                    else : positionName=0
                    print(main[0].text[positionName:])
                    print("To:"+to+'\n')
                    idComment=self.getIdComment(main[0])
                    #print("Id de comentarios:"+idComment)
                    primaryComment['idComment']=idComment
                    primaryComment['name']=names[0].text
                    primaryComment['content']=main[0].text[positionName:]
                    primaryComment['to']=to
                else:
                    print(names[0].text+":")
                    # print("IMAGEN O GIF ")
                    # primaryComment['idComment']=idComment
                    # primaryComment['name']=names[0].text
                    # primaryComment['content']="IMAGEN O GIF "
                    # primaryComment['to']="None"

                names.pop(0)

                #Respuestas
                answers = comment.find_elements_by_xpath(SEC_COMMENT)
                if answers:
                    for answer in answers:
                        secondaryComment={}
                        print("\t\t"+names[0].text+":")
                        to=self.getToName(answer)
                        if to : positionName=len(to)+1
                        else : positionName=0
                        print("\t\t"+answer.text[positionName:]+"")
                        print("\t\tTo:"+to+'\n')
                        secondaryIdComment=self.getIdComment(answer)
                        secondaryComment['IdComment']=secondaryIdComment
                        secondaryComment['name']=names[0].text
                        secondaryComment['content']=answer.text[positionName:]
                        secondaryComment['toIdComment']=idComment
                        secondaryComment['to']=to
                        secondaryComments.append(secondaryComment)
                        names.pop(0)
                else:
                    answers = comment.find_elements_by_xpath(SEC_COMMENT_GIF)
                    if answers:
                        for answer in answers:
                            secondaryComment={}
                            print("\t\t"+names[0].text+":")
                            to=self.getToName(answer)
                            if to : positionName=len(to)+1
                            else : positionName=0
                            print("\t\t"+answer.text[positionName:]+"")
                            print("\t\tTo:"+to+'\n')
                            secondaryIdComment=self.getIdComment(answer)
                            secondaryComment['IdComment']=secondaryIdComment
                            secondaryComment['name']=names[0].text
                            secondaryComment['content']=answer.text[positionName:]
                            secondaryComment['toIdComment']=idComment
                            secondaryComment['to']=to
                            secondaryComments.append(secondaryComment)
                            names.pop(0)
                    else:
                        answers = comment.find_elements_by_xpath(TRADUCT_COMMENT)
                        for answer in answers:
                            secondaryComment={}
                            print("\t\t"+names[0].text+":")
                            to=self.getToName(answer)
                            print("\t\t"+answer.text+"\n")
                            print("\t\tTo:"+to+'\n')
                            if to : positionName=len(to)+1
                            else : positionName=0
                            print("\t\t"+answer.text[positionName:]+"")
                            print("\t\tTo:"+to+'\n')
                            secondaryIdComment=self.getIdComment(answer)
                            secondaryComment['IdComment']=secondaryIdComment
                            secondaryComment['name']=names[0].text
                            secondaryComment['content']=answer.text[positionName:]
                            secondaryComment['toIdComment']=idComment
                            secondaryComment['to']=to
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
                time.sleep(2)
            except NoSuchElementException:
                t=False
                pass
