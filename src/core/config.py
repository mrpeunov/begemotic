from pydantic import BaseSettings


class Config(BaseSettings):
    RESOLUTION: int = 11
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    RELOAD: bool = True


def get_config():
    return Config()


config = get_config()
