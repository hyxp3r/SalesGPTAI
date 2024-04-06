from fastapi import APIRouter, Depends

from api.my_redis.redis import Redis
from api.schemas.chatDTO import Chat
from api.src.dependencies.messages import messages
from salesgpt.salesgptapi import SalesGPTAPI

router = APIRouter(
    prefix="/tokens"
)

redis = Redis()

@router.post("")
async def save_messages(telegram_id: str):
    chat_session = Chat(
        messages=[],
    )
    async with redis:
        await redis.set(name = str(telegram_id), obj = chat_session.model_dump(), ex=3600)
    return {"telegram_id": telegram_id}

@router.get("/chat")
async def chat_with_sales_agent(message: str, conversation_history=Depends(messages)):
    print(message, conversation_history)
    sales_api = SalesGPTAPI(
        config_path="examples/example_agent_setup.json", verbose=True
    )
    name, reply = sales_api.do(conversation_history, message)
    res = {"name": name, "say": reply}
    return res