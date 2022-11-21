from app.services import entries
from app.services.repo import BaseHouseRepo


class MockHouseRepo(BaseHouseRepo):
    storage = [
        entries.House(
            id=1000,
            geopos={'type': 'Point', 'coordinates': [37.525369, 55.531259]},
            apartments=35,
            price=255138.0,
            year=1997,
            h3="8b2cce883b5dfff"
        ),
        entries.House(
            id=1001,
            geopos={'type': 'Point', 'coordinates': [37.526762, 55.53157]},
            apartments=63,
            price=221395.0,
            year=1997,
            h3="8b2cce883b4dfff"
        ),
        entries.House(
            id=1002,
            geopos={'type': 'Point', 'coordinates': [37.525585, 55.532003]},
            apartments=46,
            price=188281.0,
            year=1997,
            h3="8b2cce883a64fff"
        ),
        entries.House(
            id=1003,
            geopos={'type': 'Point', 'coordinates': [37.527265, 55.532966]},
            apartments=197,
            price=283995.0,
            year=2001,
            h3="8b2cce881695fff"
        )
    ]

    async def get_houses_by_indexes(self, indexes: entries.H3Indexes) -> entries.Houses:
        result = []
        for house in self.storage:
            if house.h3 in indexes:
                result.append(house)
        return result
