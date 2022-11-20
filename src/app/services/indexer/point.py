from .. import entries


class PointIndexer:
    def index(self, geopos: entries.PointGeopos) -> entries.H3Indexes: ...
