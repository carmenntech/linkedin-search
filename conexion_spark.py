import pyspark
from pyspark.sql import SparkSession
import pandas as pd
from pymongo import MongoClient

# Crea una SparkSession
spark = SparkSession.builder \
    .appName("MongoSparkConnector") \
    .getOrCreate()

# Conectar a MongoDB (puedes especificar el puerto y la IP si es necesario)
client = MongoClient("mongodb://localhost:27017/")

# Seleccionar la base de datos (si no existe, MongoDB la crea automáticamente)
db = client["linkedinapi"]

# Seleccionar la colección (si no existe, MongoDB la crea automáticamente)
collection = db["borrar"]

# Extrae los datos desde MongoDB
mongo_data = list(collection.find())

# Convierte los datos a un DataFrame de pandas
pdf = pd.DataFrame(mongo_data)

# Convierte el DataFrame de pandas a un DataFrame de Spark
df = spark.createDataFrame(pdf)

# Convertir el DataFrame a un RDD
rdd = df.select("user", "views").rdd



print(rdd)