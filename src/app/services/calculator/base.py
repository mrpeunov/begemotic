from abc import ABC


from ..aggregator.base import BaseAggregator
from ..entries import AggrResult, H3Indexes
from ..repo import BaseHouseRepo


class BaseCalculator(ABC):
    repo: BaseHouseRepo
    aggregator: BaseAggregator

    def calc_by_indexes(self, h3_indexes: H3Indexes) -> AggrResult:
        houses = self.repo.get_houses_by_indexes(h3_indexes)
        return self.aggregator.aggregate(houses)
