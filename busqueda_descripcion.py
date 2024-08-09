from linkedin_api import Linkedin
from credenciales import *
import json

# Opening JSON file
with open('searchjobs.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

    for line in json_object: 
        line 


