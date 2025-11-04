from typing import List, Dict
from fastapi import UploadFile
from pydantic import BaseModel, Field
from langchain_core.messages import AnyMessage


class ChatHistory(BaseModel):
    messages: list[AnyMessage] = Field(default=[])


class UserInput(BaseModel):
    pdfs: List[UploadFile] | None
    message: str = Field(
        description="User input to the agent.",
        examples=["What is the weather in Tokyo?"],
    )
    user_id: str | None = Field(
        description="User ID to persist and continue a conversation across multiple threads.",
        default=None,
        examples=["847c6285-8fc9-4560-a83f-4e6285809254"],
    )
    thread_id: str | None = Field(
        description="Thread ID to persist and continue a multi-turn conversation.",
        default=None,
        examples=["847c6285-8fc9-4560-a83f-4e6285809254"],
    )
