import pytest

from app.repo.mock import MockHouseRepo
from app.services import entries
from app.services.aggregator import AggregationFactory
from app.services.calculator import Calculator
from app.services.indexer import PointIndexer


@pytest.mark.asyncio
async def test_calculator():
    aggr = AggregationFactory.get(field=entries.FieldEnum.APARTMENTS, aggr=entries.AggrEnum.SUM)

    calculator = Calculator(
        repo=MockHouseRepo(),
        aggregator=aggr,
        indexer=PointIndexer()
    )
    result_from_calculator = await calculator.calc(
        geopos=entries.PointGeopos(
            geometry=MockHouseRepo.storage[0].geopos,
            r=10
        )
    )
    result_from_aggr = aggr.aggregate(MockHouseRepo.storage)

    assert result_from_aggr == result_from_calculator



