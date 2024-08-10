from linkedin_api import Linkedin
from credenciales import *
import json

# Authenticate using any Linkedin account credentials
api = Linkedin(USER, PWD)

# GET a profile
profile = api.get_profile('billy-g')

# GET a profiles contact info
contact_info = api.get_profile_contact_info('billy-g')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('1234asc12304')

print(contact_info)

contact_job = api.get_job(job_id=3972627974)

print(contact_job)



#contact_jobspython = api.search_jobs(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'title': 'mongodb django', 'count': 2})




#esta parte la comento porque tarda bastante
"""
print(contact_jobspython)

with open("searchjobs.json", "w") as sj:
    json.dump(contact_jobspython, sj)
"""
