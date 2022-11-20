from .aggregator.map import get_aggregator
from .calculator import PointCalculator, PolygonCalculator
from .indexer import PointIndexer, PolygonIndexer
from src.app.services.repo import BaseHouseRepo

from . import entries


class FacadeService:
    def calculate_in_point(self, command: entries.PointAggrCommand) -> entries.AggrResult:
        aggregator = get_aggregator(
            field=command.field,
            aggr=command.aggr
        )

        return PointCalculator(
            repo=BaseHouseRepo(),
            aggregator=aggregator,
            indexer=PointIndexer()
        ).calc(geopos=command)

    def calculate_in_polygon(self, command: entries.PolygonAggrCommand) -> entries.AggrResult:
        return PolygonCalculator(
            repo=BaseHouseRepo(),
            aggregator=get_aggregator(
                field=command.field,
                aggr=command.aggr
            ),
            indexer=PolygonIndexer()
        ).calc(geopos=command)
