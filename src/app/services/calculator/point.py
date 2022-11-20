from .base import BaseCalculator
from .. import entries
from ..indexer import PointIndexer


class PointCalculator(BaseCalculator):
    indexer: PointIndexer

    def get_indexes(self, geopos: entries.PointGeopos) -> entries.H3Indexes:
        return self.indexer.index(geopos)
