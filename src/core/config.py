from pydantic import BaseSettings
import os


class Config(BaseSettings):
    RESOLUTION: int = 11
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    MONGO_URL: str = os.environ.get('MONGO_URL')


def get_config():
    return Config()


config = get_config()
