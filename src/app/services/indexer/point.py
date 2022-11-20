from .. import entries
from .base import BaseIndexer


class PointIndexer(BaseIndexer):
    def index(self, geopos: entries.PointGeopos) -> entries.H3Indexes:
        pass
