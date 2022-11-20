from fastapi import APIRouter

from src.api.contracts import responses, requests
from src.app.services.facade import FacadeService
from loguru import logger

router = APIRouter(tags=["Aggregation"])


@router.post(
    "/aggregation/point/",
    response_model=responses.AggrResultResponse,
    summary="Посчитать агрегацию в k метрах от точки",
)
async def aggregation_in_point(request: requests.PointAggrRequest):
    logger.info(f"Получен запрос {request}")
    return await FacadeService().calculate_in_point(command=request)


@router.post(
    "/aggregation/polygon/",
    response_model=responses.AggrResultResponse,
    summary="Посчитать агрегацию в заданном полигоне",
)
async def aggregation_in_point(request: requests.PolygonAggrRequest):
    logger.info(f"Получен запрос {request}")
    return await FacadeService().calculate_in_polygon(command=request)
