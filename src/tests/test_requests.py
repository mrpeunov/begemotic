import pytest
from pydantic import ValidationError
from contextlib import nullcontext as does_not_raise
from src.api.contracts.requests import PointAggrRequest


@pytest.fixture
def point_data():
    return {
        "geometry": {
            "type": "Point",
            "coordinates": [37.517259, 55.542444]
        },
        "field": "apartments",
        "aggr": "sum",
        "r": 4
    }


@pytest.mark.parametrize(
    "example_input,expectation",
    [
        (-4, pytest.raises(ValidationError)),
        (-2, pytest.raises(ValidationError)),
        (0, does_not_raise()),
        (1, does_not_raise()),
        (5, does_not_raise()),
    ],
)
def test_point_requests_radius(example_input, expectation, point_data):
    point_data["r"] = example_input

    with expectation as e:
        PointAggrRequest(**point_data)


@pytest.mark.parametrize(
    "example_input,expectation",
    [
        ("abc", pytest.raises(ValidationError)),
        ("123", pytest.raises(ValidationError)),
        ("apartments", does_not_raise()),
        ("price", does_not_raise()),
        ("year", does_not_raise()),
    ],
)
def test_point_requests_field(example_input, expectation, point_data):
    point_data["field"] = example_input

    with expectation as e:
        PointAggrRequest(**point_data)


@pytest.mark.parametrize(
    "example_input,expectation",
    [
        ("abc", pytest.raises(ValidationError)),
        ("123", pytest.raises(ValidationError)),
        ("max", does_not_raise()),
        ("min", does_not_raise()),
        ("avg", does_not_raise()),
        ("sum", does_not_raise()),
    ],
)
def test_point_requests_aggr(example_input, expectation, point_data):
    point_data["aggr"] = example_input

    with expectation as e:
        PointAggrRequest(**point_data)
