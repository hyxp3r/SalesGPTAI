from fastapi import HTTPException

from src.redis.redis import RedisGPT


async def get_telegram_id(
    telegram_id: str,
):
    redis = RedisGPT()
    async with redis:
        is_exist = await redis.is_exist(telegram_id)
    if not is_exist:
        raise HTTPException(status_code=422, detail="Telegram ID doesn't found!")
    return telegram_id
