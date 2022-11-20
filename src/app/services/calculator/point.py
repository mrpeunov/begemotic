from src.app.services.calculator.base import BaseCalculator
from src.app.services.entries import AggrResult
from src.app.services.indexer.point import PointIndexer


class PointCalculator(BaseCalculator):
    def __init__(self):
        self.indexer = PointIndexer()

    def calc(self, geopos, r) -> AggrResult:
        indexes = self.indexer.index(geopos, r)
        return self.calc_by_indexes(indexes)
