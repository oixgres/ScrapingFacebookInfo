
from init import *

data=h.get_reactions(POST_ID=2789506314634004,URL_type= "https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=")
writeJson(data,'reactions.json')