from .. import entries


class PointIndexer:
    def index(self, geopos, r) -> entries.H3Indexes: ...
