from enum import Enum
from typing import List, Union

from pydantic import BaseModel


class GeometryTypeEnum(str, Enum):
    POINT = "point"
    POLYGON = "polygon"


class GeometryModel(BaseModel):
    type: GeometryTypeEnum
    coordinates: Union[List[float], List[List[List[float]]]]  # todo перевести на python 3.10


class FieldsEnum(str, Enum):
    APARTMENTS = "apartments"
    PRICE = "price"
    YEAR = "year"


class AggrEnum(str, Enum):
    SUM = "sum"
    AVG = "avg"
    MIN = "min"
    MAX = "max"


class BaseAggrRequest(BaseModel):
    geometry: GeometryModel
    field: FieldsEnum
    aggr: AggrEnum


class PointAggrRequest(BaseAggrRequest):
    r: int

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


class PolygonAggrRequest(BaseAggrRequest):
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
