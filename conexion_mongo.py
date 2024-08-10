from pymongo import MongoClient

# Conectar a MongoDB (puedes especificar el puerto y la IP si es necesario)
client = MongoClient("mongodb://localhost:27017/")

# Seleccionar la base de datos (si no existe, MongoDB la crea automáticamente)
db = client["linkedinapi"]

# Seleccionar la colección (si no existe, MongoDB la crea automáticamente)
collection = db["borrar"]



# Insertar un documento en la colección
documento = {
    "nombre": "Juan",
    "edad": 28,
    "ciudad": "Madrid"
}

# Insertar el documento
resultado = collection.insert_one(documento)

# Imprimir el ID del documento insertado
print(f"Documento insertado con el ID: {resultado.inserted_id}")

# Buscar un documento en la colección
resultado_busqueda = collection.find_one({"nombre": "Juan"})

# Imprimir el documento encontrado
print("Documento encontrado:", resultado_busqueda)

# Actualizar un documento
collection.update_one({"nombre": "Juan"}, {"$set": {"edad": 29}})

# Eliminar un documento
#collection.delete_one({"nombre": "Juan"})

# Cerrar la conexión
client.close()

