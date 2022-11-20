from fastapi import APIRouter

from src.api.contracts import responses, requests
from src.app.services.facade import FacadeService

router = APIRouter(tags=["Aggregation"])


@router.post(
    "/aggregation/point/",
    response_model=responses.AggrResultResponse,
    summary="Посчитать агрегацию в k метрах от точки",
)
async def aggregation_in_point(request: requests.PointAggrRequest):
    return FacadeService().calculate_in_point(
        geopos=request.geometry,
        r=request.r,
        aggr=request.aggr,
        field=request.field
    )


@router.post(
    "/aggregation/polygon/",
    response_model=responses.AggrResultResponse,
    summary="Посчитать агрегацию в полигонах",
)
async def aggregation_in_point(request: requests.PolygonAggrRequest):
    return {"value": 238302.86}
