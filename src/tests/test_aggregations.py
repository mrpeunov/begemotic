import pytest

from src.app.services.aggregator import AggregationFactory
from src.app.services import entries


@pytest.fixture
def houses():
    return [
        entries.House(
            id=1000,
            geopos={'type': 'Point', 'coordinates': [37.525369, 55.531259]},
            apartments=35,
            price=255138.0,
            year=1997,
        ),
        entries.House(
            id=1001,
            geopos={'type': 'Point', 'coordinates': [37.526762, 55.53157]},
            apartments=63,
            price=221395.0,
            year=1997,
        ),
        entries.House(
            id=1002,
            geopos={'type': 'Point', 'coordinates': [37.525585, 55.532003]},
            apartments=46,
            price=188281.0,
            year=1997,
        ),
        entries.House(
            id=1003,
            geopos={'type': 'Point', 'coordinates': [37.527265, 55.532966]},
            apartments=197,
            price=283995.0,
            year=2001,
        )
    ]


def test_min(houses):
    min_aggr = AggregationFactory.get(field=entries.FieldEnum.APARTMENTS,  aggr=entries.AggrEnum.MIN)
    result = min_aggr.aggregate(houses)
    assert result.value == 35


def test_max(houses):
    max_aggr = AggregationFactory.get(field=entries.FieldEnum.APARTMENTS,aggr=entries.AggrEnum.MAX)
    result = max_aggr.aggregate(houses)
    assert result.value == 197


def test_avg(houses):
    avg_aggr = AggregationFactory.get(field=entries.FieldEnum.APARTMENTS, aggr=entries.AggrEnum.AVG)
    result = avg_aggr.aggregate(houses)
    assert result.value == 85.25


def test_sum(houses):
    sum_aggr = AggregationFactory.get(field=entries.FieldEnum.APARTMENTS, aggr=entries.AggrEnum.SUM)
    result = sum_aggr.aggregate(houses)
    assert result.value == 341


def test_year(houses):
    aggr = AggregationFactory.get(field=entries.FieldEnum.YEAR, aggr=entries.AggrEnum.MAX)
    result = aggr.aggregate(houses)
    assert result.value == 2001


def test_price(houses):
    aggr = AggregationFactory.get(field=entries.FieldEnum.PRICE, aggr=entries.AggrEnum.MAX)
    result = aggr.aggregate(houses)
    assert result.value == 283995.0


def test_price_min(houses):
    aggr = AggregationFactory.get(field=entries.FieldEnum.PRICE, aggr=entries.AggrEnum.MIN)
    result = aggr.aggregate(houses)
    assert result.value == 188281.0
