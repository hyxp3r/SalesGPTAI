from fastapi import APIRouter

from src.service.token import create_chat

router = APIRouter(prefix="/tokens")


@router.post("/creation")
async def save_messages(telegram_id: str):
    await create_chat(telegram_id)
    return {"telegram_id": telegram_id}
