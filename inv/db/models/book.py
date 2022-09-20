from dataclasses import dataclass
from bson import ObjectId
from pydantic import BaseModel

from inv.shared.models import PyObjectId
from pydantic import Field

from attrs import asdict, define, make_class, Factory


class Book(BaseModel):
    id: PyObjectId = Field(alias="_id")
    title: str
    read_date: str
    author: str | None
