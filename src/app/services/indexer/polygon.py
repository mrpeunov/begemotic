from .. import entries
from .base import BaseIndexer


class PolygonIndexer(BaseIndexer):
    def index(self, geopos) -> entries.H3Indexes:
        pass
