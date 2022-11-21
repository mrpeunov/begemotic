from src.app.services import entries
from src.app.services.repo import BaseHouseRepo


class MongoHouseRepo(BaseHouseRepo):
    def __init__(self, collection):
        self.collection = collection

    async def get_houses_by_indexes(self, indexes: entries.H3Indexes) -> entries.Houses:
        query = {"h3": {"$in": indexes}}

        houses = []
        async for house in self.collection.find(query):
            houses.append(entries.House(id=str(house["_id"]), **house))
        return houses
