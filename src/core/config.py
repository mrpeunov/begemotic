from pydantic import BaseSettings
import os


class Config(BaseSettings):
    RESOLUTION: int = 11
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    RELOAD: bool = True
    MONGO_URL: str = os.environ.get(
        'MONGO_URL',
        'mongodb+srv://my_test:WrqSDWWFEkIPuRnI@cluster0.82k1xob.mongodb.net/?retryWrites=true&w=majority'
    )


def get_config():
    return Config()


config = get_config()
