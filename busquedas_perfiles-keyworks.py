from linkedin_api import Linkedin
from credenciales import *
import json
import pandas as pd
from linkedin_api.client import Client
import pandas as pd
from pymongo import MongoClient

from linkedin_api.utils.helpers import (
    get_id_from_urn,
    get_urn_from_raw_update,
    get_list_posts_sorted_without_promoted,
    parse_list_raw_posts,
    parse_list_raw_urns,
    generate_trackingId,
    generate_trackingId_as_charString,
)
# Authenticate using any Linkedin account credentials
api = Linkedin(USER, PWD)



contact_job = api.search_people(keywords = 'Mongodb', schools='Universidad de Valladolid')


# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["linkedinapi"]
collection = db["perfiles-mogo"]

df = pd.DataFrame(contact_job)

# Insertar los datos en la colección
collection.insert_many(df.to_dict("records"))


print(contact_job)