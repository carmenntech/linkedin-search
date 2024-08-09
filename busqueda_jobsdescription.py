from linkedin_api import Linkedin
from credenciales import *
import pandas as pd
import json

api = Linkedin(USER, PWD)


keywordslist = ["Data engieneer", "Data Developer", "Cloud", "Ingeniero de datos", "Big Data", "Inteligencia artificial", "Python Developer", "Data Analyst", "Analista de datos"]


contact_jobs2 = api.search_jobs( keywords =  "Data developer" , location_name = "Spain") 
#print(contact_jobs2)
# Crear el DataFrame
df = pd.DataFrame(contact_jobs2)
df["trackingUrn"] = df["trackingUrn"].apply(lambda x: x[-10:])
df_id = df["trackingUrn"]
id_list = df_id.values.tolist()

print(id_list)

df = pd.DataFrame()


for id in id_list:

    jobpost = api.get_job(job_id=id)
    # Claves que quieres seleccionar
    keys_to_select = ["jobPostingId", "title", "entityUrn", "formattedLocation"]

    # Crear un nuevo diccionario con solo las claves seleccionadas
    selected_data = dict(zip(keys_to_select, [jobpost[key] for key in keys_to_select]))

    df = pd.concat([df, pd.DataFrame([selected_data])], ignore_index=True)

    #print(jobpost)
    #print("\n================================")
    """
        with open("prueba1.json", "w") as dj:
        json.dump(df, dj)
    """

    
    
print(df)



    #df_jobs = pd.concat([df_jobs, jobpost], ignore_index=True)





"""
with open("datajobs.json", "w") as dj:
    json.dump(contact_jobs2, dj)
"""



