from src.app.services import entries
from src.app.services.repo import BaseHouseRepo


class MockHouseRepo(BaseHouseRepo):
    def get_houses_by_indexes(self, indexes: entries.H3Indexes) -> entries.Houses:
        return [
            entries.House(
                id=1000,
                geopos={'type': 'Point', 'coordinates': [37.525369, 55.531259]},
                apartments=35,
                price=255138.0,
                year=1997
            ),
            entries.House(
                id=1001,
                geopos={'type': 'Point', 'coordinates': [37.526762, 55.53157]},
                apartments=63,
                price=221395.0,
                year=1997
            )
        ]
