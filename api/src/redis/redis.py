from typing import List

from redis import asyncio as aioredis
from redis.commands.json.path import Path

from api.config import RedisSettings

settings = RedisSettings()


class Redis:
    """
    config для подключения Redis
    """

    def __init__(self):
        self.connection_url = settings.url

    async def __aenter__(self):
        self.connection = aioredis.from_url(self.connection_url, db=0)

    async def __aexit__(self, *args):
        await self.connection.close()

    async def get(self, name: str) -> List[dict]:
        result = await self.connection.json().mget([name], Path(".conversation_history"))
        return result[0]

    async def set(self, name: str, obj: dict, ex: int = None):
        result = await self.connection.json().set(name=name, path=Path.root_path(), obj=obj)
        if ex:
            await self.connection.expire(str(name), ex)
        return result

    async def is_exist(self, key: str) -> int:
        return await self.connection.exists(key)


class RedisGPT(Redis):
    def __init__(self):
        super().__init__()

    async def get_messages(self, name: str) -> List[dict]:
        result = await self.connection.json().mget([name], Path(".conversation_history"))
        return result[0]

    async def add_message_to_cache(self, token: str, source: str, message_data: dict):
        if source == "human":
            message_data["message"] = "User: " + message_data["message"] + " <END_OF_TURN>"
        elif source == "bot":
            message_data["message"] = "Ted Lasso: " + message_data["message"] + " <END_OF_TURN>"
        await self.connection.json().arrappend(str(token), Path(".conversation_history"), message_data)
