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

    async def calc(self, geopos: entries.Geopos) -> entries.AggrResult:
        indexes = self.get_indexes(geopos)
        logger.info(f"Найденные индексы: {indexes}")
        houses = await self.repo.get_houses_by_indexes(indexes)
        logger.info(f"Найденные дома: {houses}")
        return self.aggregator.aggregate(houses)

    @abstractmethod
    def get_indexes(self, geopos: entries.Geopos) -> entries.H3Indexes: ...
