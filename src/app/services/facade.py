from src.app.services.aggregator.map import get_aggregator
from src.app.services.calculator import PointCalculator, PolygonCalculator
from src.app.services import entries
from src.app.services.repo import BaseHouseRepo


class FacadeService:
    def calculate_in_point(self, command: entries.PointAggrCommand) -> entries.AggrResult:
        return PointCalculator(
            repo=BaseHouseRepo(),
            aggregator=get_aggregator(
                field=command.field,
                aggr=command.aggr
            )
        ).calc(geopos=command.geometry, r=command.r)

    def calculate_in_polygon(self, command: entries.PolygonAggrCommand) -> entries.AggrResult:
        return PolygonCalculator(
            repo=BaseHouseRepo(),
            aggregator=get_aggregator(
                field=command.field,
                aggr=command.aggr
            )
        ).calc(geopos=command.geometry)
