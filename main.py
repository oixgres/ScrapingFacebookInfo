# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:36:09 2021

@author: Sergio
"""
from facebook_scraper import get_posts

for post in get_posts('nintendoLatAm', pages=5):
    print(post['text'][:100])