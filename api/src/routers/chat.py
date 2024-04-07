from fastapi import APIRouter, Depends

from api.src.service.chat import chat_with_sales_agent
from src.routers.dependence import get_telegram_id
from src.schemas.chat import MessageList

router = APIRouter(prefix="/chat")


@router.post("")
async def get_answer(request: MessageList, telegram_id: str = Depends(get_telegram_id)):
    answer = await chat_with_sales_agent(request, telegram_id)
    return answer
