from .aggregator import AggregationFactory, BaseAggregator
from .calculator import Calculator
from .indexer import PointIndexer, PolygonIndexer

from . import entries
from ..repo.mongo import MongoHouseRepo


class FacadeService:
    async def calculate_in_point(self, command: entries.PointAggrCommand) -> entries.AggrResult:
        return await Calculator(
            repo=MongoHouseRepo(),
            aggregator=self._get_aggregator(command),
            indexer=PointIndexer()
        ).calc(geopos=command)

    async def calculate_in_polygon(self, command: entries.PolygonAggrCommand) -> entries.AggrResult:
        return await Calculator(
            repo=MongoHouseRepo(),
            aggregator=self._get_aggregator(command),
            indexer=PolygonIndexer()
        ).calc(geopos=command)

    def _get_aggregator(self, command: entries.BaseAggrCommand) -> BaseAggregator:
        return AggregationFactory.get(
            field=command.field,
            aggr=command.aggr
        )
