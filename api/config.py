from pydantic_settings import BaseSettings


class ApiKeySettings(BaseSettings):
    api_key:str

    class Config:
        env_prefix = 'OPENAI_'
        env_file = '.env'
        extra = 'ignore'


class RedisSettings(BaseSettings):
    url: str

    class Config:
        env_prefix = 'REDIS_'
        env_file = '.env'
        extra = 'ignore'