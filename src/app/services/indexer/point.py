from .. import entries
from .base import BaseIndexer


class PointIndexer(BaseIndexer):
    def index(self, geopos: entries.PointGeopos) -> entries.H3Indexes:
        return [
            entries.H3Index('822d57fffffffff')
        ]
