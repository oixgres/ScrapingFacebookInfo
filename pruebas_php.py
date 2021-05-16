# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:49:43 2021

@author: Sergio
"""

import urllib
import urllib3
import requests

obj={'id':'prueba', 'url':'prueba', 'user':'prueba', 'text':'text'}
res = requests.post("http://conisoft.org/FacebookScraper/test_query.php", data=obj)



print(res.text)