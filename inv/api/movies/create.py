from datetime import date

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from inv.repo.movie import MovieRepo

router = APIRouter()


class CreateMovieSchema(BaseModel):
    title: str
    watch_date: date
    production_year: str | None = None
    directors: str | None = None


@router.post("/movie")
async def create_movie(movie: CreateMovieSchema):
    movie_id = await MovieRepo.create(movie)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content={"id": str(movie_id)}
    )
