from datetime import date, datetime
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel, Field
from inv.db import get_db
from inv.repo.movie import MovieRepo
from fastapi import APIRouter

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
