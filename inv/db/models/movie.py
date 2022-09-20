from datetime import date

from pydantic import BaseModel, Field

from inv.shared.models import PyObjectId


class MovieModel(BaseModel):
    id: PyObjectId = Field(alias="_id")
    title: str
    watch_date: date
    production_year: str | None = None
    directors: str | None = None
