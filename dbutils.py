from pymongo import MongoClient

#Cambio de password a admin
#MONGO_URI= "mongodb+srv://admin:admin@cluster0-o1met.mongodb.net/test"
MONGO_URI=""
#aqui empezamos a poner el código:
#programación que jala datos y los pone en el html
#delete no lo vimos pero borra colecciones
def db_connect(MONGO_URI,db_name, col_name):
    client= MongoClient(MONGO_URI)
    database=client[db_name]
    collection=database[col_name]
    return collection

def db_insert_user(collection, user):
    return collection.insert_one(user)

#si el query va vacio devuelve todo ((Read))
def db_find_all(collection, query={}):
    return collection.find(query)

if __name__ == '__main__':
    print("MongoClient imported successfully!")
