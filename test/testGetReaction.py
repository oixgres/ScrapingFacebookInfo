
from init import *

data=h.get_reactions(POST_ID=2789506314634004,URL_type= "https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=")
writeJson(data,'reactions.json')

data=h.test_User_names(2789506314634004,URL_SHARED,"shared_names")
writeJson(data,'shares.json')