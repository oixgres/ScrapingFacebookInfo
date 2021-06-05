# -*- coding: utf-8 -*-
"""
Created on Sat May 15 17:08:01 2021

@author: Sergio
"""

import requests
import json

def insertPost(values):
    res = requests.post('http://conisoft.org/FacebookScraper/insertPost.php', data=values)
    return res.text

def insertComment(values):
    res = requests.post('http://conisoft.org/FacebookScraper/insertComment.php', data=values)
    return res.text

def insert(file, values):
    res = requests.post('http://conisoft.org/FacebookScraper/'+file, data=values)
    if res.json()['res'] == 'ERROR':
        print(res.json()['error'])
        return (-1)
    else:
        print(res.json()['res'])
        return (0)