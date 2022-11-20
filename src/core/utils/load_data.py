from typing import List, Dict

import pymongo
from pymongo.server_api import ServerApi
import pandas as pd
import ast
import h3


def get_mongo_client():
    return pymongo.MongoClient(
        "mongodb+srv://my_test:WrqSDWWFEkIPuRnI@cluster0.82k1xob.mongodb.net/?retryWrites=true&w=majority",
        server_api=ServerApi('1')
    )


def get_collection():
    client = get_mongo_client()
    db = client.begemotic
    return db.houses


def load_data_from_csv() -> List[Dict]:
    df = pd.read_csv('apartments.csv')
    apartments = df.to_dict('records')

    for apartment in apartments:
        apartment['geopos'] = ast.literal_eval(apartment.get('geopos'))

    return apartments


def calculate_h3(apartments: List[Dict]):
    for apartment in apartments:
        lat = apartment['geopos']['coordinates'][0]
        lng = apartment['geopos']['coordinates'][1]
        index = h3.geo_to_h3(lat=lat, lng=lng, resolution=11)
        apartment['h3'] = index


def load_to_mongo(apartments: List[Dict]):
    collection = get_collection()
    for apartment in apartments:
        apartment["_id"] = apartment.pop("id")
        collection.insert_one(apartment)
        print(f"Добавлено {apartment}")


def load_data_from_csv_to_mongo():
    apartments = load_data_from_csv()
    calculate_h3(apartments)
    load_to_mongo(apartments)


if __name__ == '__main__':
    load_data_from_csv_to_mongo()
