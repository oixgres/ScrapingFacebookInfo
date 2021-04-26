from init import *

dataComment=h.getComments(url='https://m.facebook.com/story.php?story_fbid=2768196876764948&id=1629107234007257&anchor_composer=false')
writeJson(dataComment,'comment.json')