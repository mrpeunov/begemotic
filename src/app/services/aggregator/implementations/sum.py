from app.services.aggregator.base import BaseAggregator
from app.services.aggregator.field import FieldGetter
from app.services.entries import Houses, AggrResult


class SumAggregator(BaseAggregator):
    def __init__(self, field_getter: FieldGetter):
        self.field_getter = field_getter

    def aggregate(self, houses: Houses) -> AggrResult:
        return AggrResult(value=sum(map(self.field_getter.get, houses)))
