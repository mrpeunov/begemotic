from fastapi import APIRouter

from src.api.contracts import responses, requests

router = APIRouter(tags=["Aggregation"])


@router.post(
    "/aggregation/point/",
    response_model=responses.AggrResultResponse,
    summary="Посчитать агрегацию в k метрах от точки",
)
async def aggregation_in_point(request: requests.PointAggrRequest):
    return {"value": 1501}


@router.post(
    "/aggregation/polygon/",
    response_model=responses.AggrResultResponse,
    summary="Посчитать агрегацию в полигонах",
)
async def aggregation_in_point(request: requests.PolygonAggrRequest):
    return {"value": 238302.86}
