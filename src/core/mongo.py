import motor.motor_asyncio

from core.config import config


class MongoWrapper:
    _instance = None

    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(config.MONGO_URL)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_collection(self):
        return self.client.begemotic.houses
