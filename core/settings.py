from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str

    model_config = ConfigDict(
        env_file=".env"
    )  # 使用 model_config 替代 class ConfigDict


settings = Settings()  # type: ignore
