from dataclasses import dataclass
from datetime import date
from bson import ObjectId
from pydantic import BaseModel

from inv.shared.models import PyObjectId
from pydantic import Field

from attrs import asdict, define, make_class, Factory
import attrs


class MovieModel(BaseModel):
    id: PyObjectId = Field(alias="_id")
    title: str
    watch_date: date
    production_year: str | None = None
    directors: str | None = None
