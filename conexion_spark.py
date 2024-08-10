import pyspark
from pyspark.sql import SparkSession
import pandas as pd

# Crea una SparkSession
spark = SparkSession.builder \
    .appName("MongoSparkConnector") \
    .getOrCreate()