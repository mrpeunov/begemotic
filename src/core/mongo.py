import motor.motor_asyncio


client: motor.motor_asyncio.AsyncIOMotorClient


def init_mongo_client():
    global client
    url = "mongodb+srv://my_test:WrqSDWWFEkIPuRnI@cluster0.82k1xob.mongodb.net/?retryWrites=true&w=majority"
    client = motor.motor_asyncio.AsyncIOMotorClient(url)


def get_mongo_client():
    global client
    return client


def get_collection():
    client = get_mongo_client()
    db = client.begemotic
    return db.houses
