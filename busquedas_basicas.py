from linkedin_api import Linkedin
from credenciales import *
import json
import pandas as pd

# Authenticate using any Linkedin account credentials
api = Linkedin(USER, PWD)

# GET a profile
#profile = api.get_profile('billy-g')

# GET a profiles contact info
#contact_info = api.get_profile_contact_info('billy-g')

# GET 1st degree connections of a given profile
#connections = api.get_profile_connections('1234asc12304')

#print(contact_info)

contact_job = api.get_job(job_id=3944659163)
contact_jobs2 = api.search_jobs( remote = '2')

print(contact_jobs2)
#print(contact_job)
description = contact_job["description"]["text"] 
jobPostingId = contact_job["jobPostingId"] 
title = contact_job["title"]
entityUrn = contact_job["entityUrn"] 
formattedLocation = contact_job["formattedLocation"] 

df = pd.DataFrame({'jobPostingId': [jobPostingId],  'title': [title], 'description': [description],  'entityUrn': [entityUrn], 'formattedLocation': [formattedLocation]})


# Mostrar el DataFrame
#print(contact_job)

print("****************************************************************")

#print(df["description"])

#print(text)

##keys_to_select = str(["jobPostingId", "title", "entityUrn"]) + str(["description"]["text"])

# Crear un nuevo diccionario con solo las claves seleccionadas
#selected_data = dict(zip(keys_to_select, [contact_job[key] for key in keys_to_select]))


#print(keys_to_select)

#contact_jobspython = api.search_jobs(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'title': 'mongodb django', 'count': 2})




#esta parte la comento porque tarda bastante
"""
print(contact_jobspython)

with open("searchjobs.json", "w") as sj:
    json.dump(contact_jobspython, sj)
"""
