from src.redis.redis import RedisGPT
from src.schemas.chat import Chat, Message


async def add_message_redis(telegram_id: str, source: str, message: Message):
    redis = RedisGPT()
    async with redis:
        await redis.add_message_to_cache(telegram_id, source, message.model_dump())


async def get_chat_history_redis(telegram_id: str) -> list[str]:
    redis = RedisGPT()
    async with redis:
        messages = await redis.get_messages(telegram_id)
    return Chat(conversation_history=messages)
