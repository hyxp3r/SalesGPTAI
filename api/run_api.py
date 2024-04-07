from fastapi import FastAPI
import uvicorn


from api.config import ApiKeySettings
from src.routers.chat import router as chat_router
from src.routers.messages import router as message_router
from src.routers.tokens import router as token_router

api_settings = ApiKeySettings()
app = FastAPI()

app.include_router(token_router)
app.include_router(message_router)
app.include_router(chat_router)


GPT_MODEL = "gpt-3.5-turbo-0613"
# GPT_MODEL_16K = "gpt-3.5-turbo-16k-0613"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
