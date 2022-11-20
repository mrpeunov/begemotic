from abc import ABC, abstractmethod

from loguru import logger

from .. import entries
from ..aggregator import BaseAggregator
from ..indexer import BaseIndexer
from ..repo import BaseHouseRepo


class BaseCalculator(ABC):
    def __init__(self, repo: BaseHouseRepo, aggregator: BaseAggregator, indexer: BaseIndexer):
        self.repo = repo
        self.aggregator = aggregator
        self.indexer = indexer

    def calc(self, geopos: entries.Geopos) -> entries.AggrResult:
        indexes = self.get_indexes(geopos)
        logger.info(f"Найденные индексы: {indexes}")
        return self._calc_by_indexes(indexes)

    def _calc_by_indexes(self, indexes: entries.H3Indexes) -> entries.AggrResult:
        houses = self.repo.get_houses_by_indexes(indexes)
        logger.info(f"Найденные дома: {houses}")
        return self.aggregator.aggregate(houses)

    @abstractmethod
    def get_indexes(self, geopos: entries.Geopos) -> entries.H3Indexes: ...
