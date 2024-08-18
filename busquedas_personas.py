from linkedin_api import Linkedin
from credenciales import *
import json
import pandas as pd
from linkedin_api.client import Client
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



contact_job = api.search_people(keywords = 'Mongodb')


print(contact_job)