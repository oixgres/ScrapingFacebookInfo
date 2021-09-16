import requests
import json

def insert(file, values):
    res = requests.post('http://conisoft.org/FacebookScraper/'+file, data=values)
    if res.json()['res'] == 'ERROR':
        print(res.json()['error'])
        return (-1)
    else:
        print(res.json()['res'])
        return (0)