from src.app.services.aggregator.base import BaseAggregator
from src.app.services.aggregator.field import FieldGetter
from src.app.services.entries import Houses, AggrResult


class MinAggregator(BaseAggregator):
    def __init__(self, field_getter: FieldGetter):
        self.field_getter = field_getter

    def aggregate(self, houses: Houses) -> AggrResult:
        return AggrResult(value=min(map(self.field_getter.get, houses)))
