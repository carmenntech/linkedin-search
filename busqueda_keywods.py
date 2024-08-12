from linkedin_api import Linkedin
from credenciales import *
import pandas as pd
from pymongo import MongoClient
import json

api = Linkedin(USER, PWD)


keywordslist = ["Data engieneer", "Data Developer", "Cloud", "Ingeniero de datos", "Big Data", "Inteligencia artificial", "Python Developer", "Data Analyst", "Analista de datos"]


contact_jobs2 = api.search_jobs( keywords =  "sql" , location_name = "Spain")  #, location_name = "Spain"
#print(contact_jobs2)
# Crear el DataFrame
df = pd.DataFrame(contact_jobs2)
df["trackingUrn"] = df["trackingUrn"].apply(lambda x: x[-10:])
df_id = df["trackingUrn"]
id_list = df_id.values.tolist()

print(id_list)

# Crear una lista para almacenar las filas
rows = []

for id in id_list:
    jobpost = api.get_job(job_id=id)
    description = jobpost["description"]["text"]
    jobPostingId = jobpost["jobPostingId"]
    title = jobpost["title"]
    entityUrn = jobpost["entityUrn"]
    formattedLocation = jobpost["formattedLocation"]
    
    # Añadir un nuevo diccionario con los datos a la lista de filas
    rows.append({
        "jobPostingId": jobPostingId,
        "title": title,
        "description": description,
        "entityUrn": entityUrn,
        "formattedLocation": formattedLocation
    })
    
# Convertir la lista de filas en un DataFrame
df = pd.DataFrame(rows)

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["linkedin-docker"]
collection = db["keywords"]

# Insertar los datos en la colección
collection.insert_many(df.to_dict("records"))

