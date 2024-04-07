from src.exceptions.redis import ChatCreationError
from src.redis.redis import Redis
from src.schemas.chat import Chat


async def create_chat(telegram_id: str):
    chat_session = Chat(
        conversation_history=[],
    )
    redis = Redis()
    try:
        async with redis:
            await redis.set(name=str(telegram_id), obj=chat_session.model_dump(), ex=3600)
    except Exception:
        raise ChatCreationError
