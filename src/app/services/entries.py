from enum import Enum
from typing import Union, Sequence, Optional

from pydantic import BaseModel
from pydantic.types import NonNegativeInt
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
    h3: Optional[str]


# aliases


class H3Index(str):
    pass


Number = Union[float, int]
Houses = Sequence[House]
H3Indexes = Sequence[H3Index]


class Geopos(BaseModel):
    pass


class PointGeopos(Geopos):
    geometry: Point
    r: NonNegativeInt


class PolygonGeopos(Geopos):
    geometry: Polygon


# commands and results


class BaseAggrCommand(BaseModel):
    field: FieldEnum
    aggr: AggrEnum


class PointAggrCommand(BaseAggrCommand, PointGeopos):
    pass


class PolygonAggrCommand(BaseAggrCommand, PolygonGeopos):
    pass


class AggrResult(BaseModel):
    value: Number
