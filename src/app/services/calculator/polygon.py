from .base import BaseCalculator
from .. import entries
from ..indexer import PolygonIndexer


class PolygonCalculator(BaseCalculator):
    indexer: PolygonIndexer

    def get_indexes(self, geopos: entries.PolygonGeopos) -> entries.H3Indexes:
        return self.indexer.index(geopos=geopos)
