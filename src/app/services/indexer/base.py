from abc import ABC, abstractmethod

from geojson_pydantic import Point

from .. import entries


class BaseIndexer(ABC):
    @abstractmethod
    def index(self, geopos: Point, **kwargs) -> entries.H3Indexes: ...
