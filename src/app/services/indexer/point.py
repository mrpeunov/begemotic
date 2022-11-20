import h3

from .. import entries
from .base import BaseIndexer
from loguru import logger
from src.core import config


class PointIndexer(BaseIndexer):
    def index(self, geopos: entries.PointGeopos) -> entries.H3Indexes:
        main_index = h3.geo_to_h3(
            lat=geopos.geometry.coordinates[0],
            lng=geopos.geometry.coordinates[1],
            resolution=config.RESOLUTION
        )
        indexes = h3.k_ring(h=main_index, k=geopos.r)
        logger.info(f"Geopos: {geopos}; H3: {indexes}")
        return [entries.H3Index(index) for index in indexes]
