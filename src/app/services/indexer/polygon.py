import h3
from loguru import logger

from core.config import config
from .. import entries
from .base import BaseIndexer


class PolygonIndexer(BaseIndexer):
    def index(self, geopos: entries.PolygonGeopos) -> entries.H3Indexes:
        indexes = h3.polyfill(geopos.geometry.dict(), res=config.RESOLUTION)
        logger.info(f"Geopos: {geopos}; H3-count: {len(indexes)}; H3: {indexes};")
        return list(indexes)
