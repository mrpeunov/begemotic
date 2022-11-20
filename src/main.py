import sys
import uvicorn
from fastapi import FastAPI

from src.api.handlers import router
from loguru import logger
from src.core.config import config
from src.core.mongo import init_mongo_client

app = FastAPI()


@app.on_event("startup")
def startup():
    app.include_router(router)
    init_mongo_client()
    logger.add(sys.stdout, format="{time} {level} {message}", filter="my_module", level="INFO")


if __name__ == "__main__":
    uvicorn.run(
        "server.app:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=config.RELOAD
    )
