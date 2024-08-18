from linkedin_api import Linkedin
from datetime import datetime
from credenciales import *
import pandas as pd
from pymongo import MongoClient
import json

api = Linkedin(USER, PWD)


keywordsCloud = ["Amazon Web Service", "Azure",  "Google Cloud"]
keywordsSql = ["sql", "nosql"]
keywordsLenguaje = ["python", "r", "scala"]
keywordsReporting = ["Power bi", "Tableau"]

total = 0
rows = []
rows2 = []
rows3 = []
rows4 = []

for keywordb in keywordsCloud:
    contact_jobs = api.search_jobs( keywords =  keywordb)  #, location_name = "Spain"
    total = len(contact_jobs)
    fecha = datetime.now()

    rows.append({
        "keyword": keywordb,
        "total": total,
        "fecha": fecha,
        "grupo": 1,
    })

for keyword2 in keywordsSql:
    contact_jobs = api.search_jobs( keywords = keyword2)  #, location_name = "Spain"
    total = len(contact_jobs)
    fecha = datetime.now()

    rows2.append({
        "keyword": keyword2,
        "total": total,
        "fecha": fecha,
        "grupo": 2,
    })

for keyword3 in keywordsLenguaje:
    contact_jobs = api.search_jobs( keywords = keyword3)  #, location_name = "Spain"
    total = len(contact_jobs)
    fecha = datetime.now()

    rows3.append({
        "keyword": keyword3,
        "total": total,
        "fecha": fecha,
        "grupo": 3,
    })

for keyword4 in keywordsReporting:
    contact_jobs = api.search_jobs( keywords = keyword4)  #, location_name = "Spain"
    total = len(contact_jobs)
    fecha = datetime.now()

    rows4.append({
        "keyword": keyword4,
        "total": total,
        "fecha": fecha,
        "grupo": 4,
    })

# Convertir la lista de filas en un DataFrame
df = pd.DataFrame(rows)
df = pd.DataFrame(rows2)
df = pd.DataFrame(rows3)
df = pd.DataFrame(rows4)

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["linkedinapi"]
collection = db["keywords"]

# Insertar los datos en la colección
collection.insert_many(df.to_dict("records"))