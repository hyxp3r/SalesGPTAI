from fastapi import APIRouter, Depends

from src.routers.dependence import get_telegram_id
from src.service.redis import get_chat_history_redis

router = APIRouter(prefix="/messages")


@router.get("")
async def get_chat_history(telegram_id: str = Depends(get_telegram_id)):
    return await get_chat_history_redis(telegram_id)
