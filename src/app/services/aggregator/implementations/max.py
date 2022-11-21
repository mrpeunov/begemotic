from app.services.aggregator.base import BaseAggregator
from app.services.aggregator.field import FieldGetter
from app.services.entries import Houses, AggrResult


class MaxAggregator(BaseAggregator):
    def __init__(self, field_getter: FieldGetter):
        self.field_getter = field_getter

    def aggregate(self, houses: Houses) -> AggrResult:
        return AggrResult(value=max(map(self.field_getter.get, houses)))
