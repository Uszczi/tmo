from pydantic import BaseModel, Field

from inv.shared.models import PyObjectId


class Book(BaseModel):
    id: PyObjectId = Field(alias="_id")
    title: str
    read_date: str
    author: str | None
