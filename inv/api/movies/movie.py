from datetime import date
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from inv.api.base import BaseApiResponse
from inv.queries.movie import MovieQuery
from inv.repo.movie import MovieRepo
from inv.shared.models import PyObjectId

router = APIRouter()


class MovieModel(BaseApiResponse):
    id: PyObjectId = Field(..., alias="_id")
    title: str
    watch_date: Any
    production_year: str | None = None
    directors: str | None = None


@router.get(
    "/movies",
    response_model=list[MovieModel],
    response_model_by_alias=False,
)
async def list_movies():
    return await MovieQuery.get_all()


@router.get(
    "/movie/{id}",
    response_model=MovieModel,
    response_model_by_alias=False,
)
async def get_movie(id: str):
    try:
        return await MovieQuery.get(id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Student {id} not found")


class UpdatedMovie(BaseModel):
    title: str | None
    watch_date: date | None
    production_year: str | None
    directors: str | None

    def to_update(self) -> dict:
        return self.dict(exclude_unset=True)


@router.put("/movie/{id}")
async def update_movie(id: str, movie: UpdatedMovie):
    await MovieRepo.update(id, movie)
