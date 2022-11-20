from .base import BaseAggregator
from .field import FieldGetter
from .implementations import (
    MinAggregator,
    MaxAggregator,
    SumAggregator,
    AvgAggregator
)
from ..entries import FieldEnum, AggrEnum


class AggregationFactory:
    AGGR_MAP = {
        AggrEnum.AVG: AvgAggregator,
        AggrEnum.SUM: SumAggregator,
        AggrEnum.MIN: MinAggregator,
        AggrEnum.MAX: MaxAggregator
    }

    @classmethod
    def get(cls, field: FieldEnum, aggr: AggrEnum) -> BaseAggregator:
        field_getter = FieldGetter(field)
        aggregator_class = cls.AGGR_MAP[aggr]
        aggregator = aggregator_class(field_getter=field_getter)
        return aggregator
