import os
from typing import List, Dict

import csv
import ast
import h3
from loguru import logger
from core.config import config


class DataLoader:
    def __init__(self, collection):
        self.collection = collection

    async def load(self):
        if (size := await self._collection_size()) == 0:
            apartments = self._get_from_csv()
            self._calculate_h3(apartments)
            self._load_to_mongo(apartments)
        else:
            logger.info(f"{size} объектов уже были загружены")

    def _get_from_csv(self) -> List[Dict]:

        with open('./src/static/apartments.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            apartments = []

            next(reader)
            for row in reader:
                apartments.append({
                    "id": row[0],
                    "geopos": ast.literal_eval(row[1]),
                    "apartments": row[2],
                    "price": row[3],
                    "year": row[4]
                })

            return apartments

    def _load_to_mongo(self, apartments: List[Dict]):
        for apartment in apartments:
            apartment["_id"] = apartment.pop("id")
        self.collection.insert_many(apartments)
        logger.info(f"Загружены {len(apartments)} объектов")

    def _calculate_h3(self, apartments: List[Dict]):
        for apartment in apartments:
            lat = apartment['geopos']['coordinates'][0]
            lng = apartment['geopos']['coordinates'][1]
            index = h3.geo_to_h3(lat=lat, lng=lng, resolution=config.RESOLUTION)
            apartment['h3'] = index

    async def _collection_size(self) -> int:
        return await self.collection.estimated_document_count()
