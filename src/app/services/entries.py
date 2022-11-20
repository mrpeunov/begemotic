from enum import Enum
from typing import Union, Sequence
from pydantic import BaseModel
from geojson_pydantic import Point, Polygon


# enums


class FieldEnum(str, Enum):
    APARTMENTS = "apartments"
    PRICE = "price"
    YEAR = "year"


class AggrEnum(str, Enum):
    SUM = "sum"
    AVG = "avg"
    MIN = "min"
    MAX = "max"


# entries


class House(BaseModel):
    id: int
    geopos: Point
    apartments: int
    price: float
    year: int


# aliases


class H3Index(str):
    pass


Number = Union[float, int]
Houses = Sequence[House]
H3Indexes = Sequence[H3Index]


# commands and results


class BaseAggrCommand(BaseModel):
    field: FieldEnum
    aggr: AggrEnum


class PointAggrCommand(BaseAggrCommand):
    geometry: Point
    r: int


class PolygonAggrCommand(BaseAggrCommand):
    geometry: Polygon


class AggrResult(BaseModel):
    value: Number
