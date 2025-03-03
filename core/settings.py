from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
