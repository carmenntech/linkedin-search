from linkedin_api import Linkedin
from credenciales import *
import pandas as pd
import json

api = Linkedin(USER, PWD)

contact_job = api.get_job(job_id=3978495749)



#print(df)

# Claves que quieres seleccionar
keys_to_select = ["jobPostingId", "title", "formattedLocation"]

# Crear un nuevo diccionario con solo las claves seleccionadas
selected_data = dict(zip(keys_to_select, [contact_job[key] for key in keys_to_select]))




print(selected_data)