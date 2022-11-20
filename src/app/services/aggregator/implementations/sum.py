from src.app.services.aggregator.base import BaseAggregator
from src.app.services.aggregator.field import FieldGetter
from src.app.services.entries import Houses, AggrResult


class SumAggregator(BaseAggregator):
    def __init__(self, field_getter: FieldGetter):
        self.field_getter = field_getter

    def aggregate(self, houses: Houses) -> AggrResult:
        for i in houses:
            print(i.id, i.apartments)
        return AggrResult(value=sum(map(self.field_getter.get, houses)))
