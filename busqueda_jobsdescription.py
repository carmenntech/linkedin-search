from linkedin_api import Linkedin
from credenciales import *
import pandas as pd
import json

api = Linkedin(USER, PWD)


keywordslist = ["Data engieneer", "Data Developer", "Cloud", "Ingeniero de datos", "Big Data", "Inteligencia artificial", "Python Developer", "Data Analyst", "Analista de datos"]


contact_jobs2 = api.search_jobs( keywords =  "Data Developer" , location_name = "%Madrid%") 

#print(contact_jobs2)

# Crear el DataFrame
df = pd.DataFrame(contact_jobs2)

df["trackingUrn"] = df["trackingUrn"].apply(lambda x: x[-10:])

print(df)


"""
with open("datajobs.json", "w") as dj:
    json.dump(contact_jobs2, dj)
"""



