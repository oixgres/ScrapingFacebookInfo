
import json
import re

def writeJson(data,file):
    file = open(file,'w+',encoding="utf-8")
    json.dump(data,file,indent=4, ensure_ascii=False)
    file.close()

def readJson(file):
    with open(file,encoding='utf-8') as f:
        data_json = json.loads(f.read())
    return data_json