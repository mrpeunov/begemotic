from .base import BaseAggregator
from .field import FieldGetter
from .implementations import (
    MinAggregator,
    MaxAggregator,
    SumAggregator,
    AvgAggregator
)
from ..entries import FieldEnum, AggrEnum

aggr_map = {
    AggrEnum.AVG: AvgAggregator,
    AggrEnum.SUM: SumAggregator,
    AggrEnum.MIN: MinAggregator,
    AggrEnum.MAX: MaxAggregator
}


def get_aggregator(field: FieldEnum, aggr: AggrEnum) -> BaseAggregator:  # todo переделать на фабрику
    field_getter = FieldGetter(field)
    aggregator_class = aggr_map[aggr]
    aggregator = aggregator_class(field_getter=field_getter)
    return aggregator
