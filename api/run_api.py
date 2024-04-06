import os
from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

#from api.config import ApiKeySettings
from salesgpt.salesgptapi import SalesGPTAPI

from src.routers.chat import router
#api_settings = ApiKeySettings()
app = FastAPI()

app.include_router(router)

GPT_MODEL = "gpt-3.5-turbo-0613"
# GPT_MODEL_16K = "gpt-3.5-turbo-16k-0613"


@app.get("/")
async def say_hello():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
