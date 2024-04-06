from fastapi import HTTPException
from api.my_redis.redis import Redis


redis = Redis()


async def messages(telegram_id: str | None):
    if not telegram_id:
        raise HTTPException(status_code=422)
    async with redis:
        conversation_history_exist = await redis.is_exist(telegram_id)
        if not conversation_history_exist:
            raise HTTPException(status_code=404, detail="token not found")
        conversation_history = await redis.get(telegram_id)

    return conversation_history["messages"]
