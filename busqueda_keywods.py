from linkedin_api import Linkedin
from credenciales import *
import json

api = Linkedin(USER, PWD)

contact_job = api.get_job(job_id=3978495749)

print(contact_job)

contact_jobs2 = api.search_jobs( keywords =  "Cloud" , location_name = "*Spain*")

print(contact_jobs2)



with open("datajobs.json", "w") as dj:
    json.dump(contact_jobs2, dj)

