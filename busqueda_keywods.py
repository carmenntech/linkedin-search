from linkedin_api import Linkedin
from credenciales import *
import pandas as pd
from pymongo import MongoClient
import json

api = Linkedin(USER, PWD)


keywordslist = ["Data engieneer", "Data Developer", "Cloud", "Ingeniero de datos", "Big Data", "Inteligencia artificial", "Python Developer", "Data Analyst", "Analista de datos"]


contact_jobs2 = api.search_jobs( keywords =  "python" , location_name = "Spain") 
#print(contact_jobs2)
# Crear el DataFrame
df = pd.DataFrame(contact_jobs2)
df["trackingUrn"] = df["trackingUrn"].apply(lambda x: x[-10:])
df_id = df["trackingUrn"]
id_list = df_id.values.tolist()

print(id_list)

df = pd.DataFrame(columns=["jobPostingId", "title", "description", "entityUrn","formattedLocation"])


for id in id_list:

    jobpost = api.get_job(job_id=id)

    description = jobpost["description"]["text"] 
    jobPostingId = jobpost["jobPostingId"] 
    title = jobpost["title"]
    entityUrn = jobpost["entityUrn"] 
    formattedLocation = jobpost["formattedLocation"]
    
    # Crear una serie para la fila a añadir
    new_row = pd.Series(
        {
            "jobPostingId": jobPostingId,
            "title": title,
            "description": description,
            "entityUrn": entityUrn,
            "formattedLocation": formattedLocation
        }
    )

    # Añadir la serie al DataFrame
    
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Conectar a MongoDB (puedes especificar el puerto y la IP si es necesario)
    client = MongoClient("mongodb://localhost:27017/")

    # Seleccionar la base de datos (si no existe, MongoDB la crea automáticamente)
    db = client["linkedinapi"]

    # Seleccionar la colección (si no existe, MongoDB la crea automáticamente)
    collection = db["cloud"]

    #df = pd.concat([df, pd.DataFrame([selected_data])], ignore_index=True)

    # Convertir el DataFrame a una lista de diccionarios
    data_dict = df.to_dict("records")

    # Insertar los datos en la colección
    collection.insert_many(data_dict)

   

    #print(jobpost)
    #print("\n================================")
    """
        with open("prueba1.json", "w") as dj:
        json.dump(df, dj)
    """

    
    
print(df)