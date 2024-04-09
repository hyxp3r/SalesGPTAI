from datetime import datetime
from typing import List
import uuid

from pydantic import BaseModel


class Message(BaseModel):
    id: str = str(uuid.uuid4())
    message: str
    timestamp: str = str(datetime.now())


class Chat(BaseModel):
    conversation_history: List[Message]

    def get_conversation_history_str(self) -> list[str]:
        return [message.message for message in self.conversation_history]


class MessageList(Chat):
    human_say: str
