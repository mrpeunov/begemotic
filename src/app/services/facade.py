from .aggregator import AggregationFactory
from .calculator import PointCalculator, PolygonCalculator
from .indexer import PointIndexer, PolygonIndexer

from . import entries
from ..repo.mongo import MongoHouseRepo


class FacadeService:
    def calculate_in_point(self, command: entries.PointAggrCommand) -> entries.AggrResult:
        aggregator = AggregationFactory.get(
            field=command.field,
            aggr=command.aggr
        )

        return PointCalculator(
            repo=MongoHouseRepo(),
            aggregator=aggregator,
            indexer=PointIndexer()
        ).calc(geopos=command)

    def calculate_in_polygon(self, command: entries.PolygonAggrCommand) -> entries.AggrResult:
        aggregator = AggregationFactory.get(
            field=command.field,
            aggr=command.aggr
        )

        return PolygonCalculator(
            repo=MongoHouseRepo(),
            aggregator=aggregator,
            indexer=PolygonIndexer()
        ).calc(geopos=command)
