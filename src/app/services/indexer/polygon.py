import h3

from src.core import config
from .. import entries
from .base import BaseIndexer


class PolygonIndexer(BaseIndexer):
    def index(self, geopos: entries.PolygonGeopos) -> entries.H3Indexes:
        indexes = h3.polyfill(geopos.geometry.dict(), res=config.RESOLUTION)
        return list(indexes)
