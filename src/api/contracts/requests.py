from src.app.services import entries


class PointAggrRequest(entries.PointAggrCommand):
    class Config:
        schema_extra = {
            "example": {
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.517259, 55.542444]
                },
                "field": "apartments",
                "aggr": "sum",
                "r": 4
            }
        }


class PolygonAggrRequest(entries.PolygonAggrCommand):
    class Config:
        schema_extra = {
            "example": {
                 "geometry": {
                     "type": "Polygon",
                     "coordinates": [[
                         [37.520123, 55.54413],
                         [37.515671, 55.54399],
                         [37.514662, 55.541793],
                         [37.521218, 55.542612],
                         [37.520123, 55.54413]
                     ]]
                 },
                 "field": "price",
                 "aggr": "avg"
            }
        }
