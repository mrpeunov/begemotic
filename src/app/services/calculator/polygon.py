from src.app.services.calculator.base import BaseCalculator
from src.app.services.entries import AggrResult
from src.app.services.indexer.polygon import PolygonIndexer


class PolygonCalculator(BaseCalculator):
    def __init__(self):
        self.indexer = PolygonIndexer()

    def calc(self, geopos) -> AggrResult:
        indexes = self.indexer.index(geopos)
        return self.calc_by_indexes(indexes)
