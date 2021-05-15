# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:49:43 2021

@author: Sergio
"""

import urllib
import urllib3
import requests

res = requests.get("http://conisoft.org/FacebookScraper/connection.php")

print(res.text)