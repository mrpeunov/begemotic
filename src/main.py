import sys

from fastapi import FastAPI

from src.api.handlers import router
from loguru import logger


app = FastAPI()
app.include_router(router)
logger.add(sys.stdout, format="{time} {level} {message}", filter="my_module", level="INFO")
