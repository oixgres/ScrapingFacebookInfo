from init import *
json_post=h.collectionPOST(URL_GROUP,10)
writeJson(json_post,'post.json')
json_post=readJson('post.json')