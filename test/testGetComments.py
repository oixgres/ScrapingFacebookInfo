from init import *
'''
import pymysql
connection = pymysql.connect(host = "174.136.52.201", user="conisoft_fb", password = "Fengoigres1094346", database = "conisoft_facebook_scraper")
cursor = connection.cursor()
dataComment=h.getComments(url='https://m.facebook.com/groups/413938496303058/permalink/',postId=469954730701434)
writeJson(dataComment,'comment.json')
data=h.collectionPOST(URL_GROUP,10)
for index in range(len(data)):
    query = "INSERT INTO POST(post_id, poster_name, post_text, link) VALUES(%s, %s, %s, %s);"
    cursor.execute(query, (data[index]['post_id'],data[index]['poster_name'],data[index]['post_text'],data[index]['link']));

for index in range(len(data)):
    dataComment=h.getComments(url=URL_POST_LINK,postId=data[index]['post_id'])
    for comment in dataComment:
        query = "INSERT INTO Comentarios(idComentarios, post_id, persona, texto) VALUES(%s, %s, %s, %s);"
        if comment['primaryComment']:
            cursor.execute(query, (comment['primaryComment']['idComment'],
                                    comment['primaryComment']['postId'],
                                    comment['primaryComment']['name'],
                                    comment['primaryComment']['content']));
        else :
            print('No hay dato')
# data = readJson('comment.json')
# print(data)
# query = "INSERT INTO Respuesta(idRespuesta, persona, texto, idComentario,para,post_id) VALUES(%s, %s, %s, %s, %s, %s);"
# cursor.execute(query, (data[0]['secondaryComment'][0]['IdComment'],
#                         data[0]['secondaryComment'][0]['name'],data[0]['secondaryComment'][0]['content'],
#                         data[0]['secondaryComment'][0]['toIdComment'],
#                         data[0]['secondaryComment'][0]['to'],
#                         data[0]['secondaryComment'][0]['postId']));
 
connection.close()
'''
h.getComments(url='https://m.facebook.com/groups/413938496303058/permalink/469954730701434', postId=469954730701434)
