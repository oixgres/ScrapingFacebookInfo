from init import *

data=h.getComments(url='https://m.facebook.com/groups/413938496303058/permalink/', postId=433685554328352)
writeJson(data,"comments.json")

