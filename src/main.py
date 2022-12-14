import sys

import uvicorn
from fastapi import FastAPI

from api.handlers import router
from loguru import logger
from core.config import config
from core.mongo import MongoWrapper
from core.utils.load_data import DataLoader

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.include_router(router)
    logger.add(sys.stdout, format="{time} {level} {message}", filter="my_module", level="INFO")
    collection = MongoWrapper().get_collection()
    await DataLoader(collection).load()


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=False
    )
