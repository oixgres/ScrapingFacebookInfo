# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:36:09 2021

@author: Sergio

Necesitas instalar previamente facebook-scrapper y PyCLI

"""

import csv
from facebook_scraper import get_posts

"""
for post in get_posts('nintendoLatAm', pages=5):
    print(post['text'][:100])
    
with open('prueba.csv', 'w', encoding='UTF8') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Baked Beans', 'Wonderful Spam'])

print("Listo")
"""


for post in get_posts('NintendoLatAm', pages=5):
    print(post['text'][:100])
    print(post['comments'])

with open('prueba.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    
    for post in get_posts('NintendoLatAm', pages=10):
        writer.writerow([post['text'][:100],post['comments']])

print("Listo")

#facebook-scraper --filename nintendo_page_posts.csv --pages 10 nintendo

