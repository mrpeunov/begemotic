from src.app.services import entries
from src.app.services.repo import BaseHouseRepo
from src.core.mongo import get_collection


class MongoHouseRepo(BaseHouseRepo):
    async def get_houses_by_indexes(self, indexes: entries.H3Indexes) -> entries.Houses:
        collection = get_collection()
        query = {"h3": {"$in": indexes}}

        houses = []
        async for house in collection.find(query):
            houses.append(entries.House(
                id=str(house["_id"]),
                **house
            ))
        return houses
