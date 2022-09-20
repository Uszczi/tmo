from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import Field

from inv.api.base import BaseApiResponse
from inv.queries.movie import MovieQuery
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


# @router.delete("/movie/{id}")
# async def delete_movie(id: str):
#     try:
#         await MovieQuery.delete(id)
#     except Exception:
#         raise HTTPException(status_code=404, detail=f"Student {id} not found")
