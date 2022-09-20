from dataclasses import dataclass
from bson import ObjectId
from pydantic import BaseModel

from inv.shared.models import PyObjectId
from pydantic import Field

from attrs import asdict, define, make_class, Factory


@define
class Book:
    id: str
    title: str
    read_date: str
    author: str | None
