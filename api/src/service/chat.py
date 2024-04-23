from salesgpt.salesgptapi import SalesGPTAPI

from src.schemas.chat import Message, MessageList
from src.service.redis import add_message_redis


async def chat_with_sales_agent(request: MessageList, telegram_id: str) -> str:
    sales_api = SalesGPTAPI(config_path="api/examples/example_agent_setup.json", verbose=True)
    _, answer = sales_api.do(request.get_conversation_history_str(), request.human_say)
    human_say = Message(message=request.human_say)
    answer = Message(message=answer)
    await add_message_redis(telegram_id, "human", human_say)
    await add_message_redis(telegram_id, "bot", answer)
    return answer
