import pymongo
from pymongo.server_api import ServerApi


def get_mongo_client():
    return pymongo.MongoClient(
        "mongodb+srv://my_test:WrqSDWWFEkIPuRnI@cluster0.82k1xob.mongodb.net/?retryWrites=true&w=majority",
        server_api=ServerApi('1')
    )


def get_collection():
    client = get_mongo_client()
    db = client.begemotic
    return db.houses
