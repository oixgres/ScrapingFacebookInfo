import string
cadena = 'Angelina H. Cortés las tarjetas de amiibo si'
to ='Angelina H. Cortés'

id={}
id['31312412341233']=True
id['313412341234']=False
try:
    if id['313412341234'] is not None:print(id)
except :
    print("no hay nada")