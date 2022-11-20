from src.app.services.calculator import PointCalculator, PolygonCalculator
from src.app.services.entries import AggrResult


class FacadeService:
    def calculate_in_point(self, geometry, r, aggr, field) -> AggrResult:
        return PointCalculator().calc(geopos, r)

    def calculate_in_polygon(self, geopos, aggr, field) -> AggrResult:
        return PolygonCalculator().calc(geopos)
