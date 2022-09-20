from fastapi import FastAPI, Body, HTTPException, status
from datetime import date
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Any, Optional, List
from inv.db import get_db
from inv.queries.movie import MovieQuery

from inv.shared.models import PyObjectId

from fastapi import APIRouter

router = APIRouter(tags=["movies"])

db = get_db()


class BaseApiResponse(BaseModel):
    class Config:
        json_encoders = {ObjectId: str}


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
    movies = await MovieQuery.get_all()
    return movies


@router.get(
    "/movie/{id}",
    response_model=MovieModel,
    response_model_by_alias=False,
)
async def get_movie(id: str):
    try:
        movie = await MovieQuery.get(id)
        return movie
    except Exception:
        raise HTTPException(status_code=404, detail=f"Student {id} not found")


@router.delete("/movie/{id}")
async def delete_movie(id: str):
    try:
        await MovieQuery.delete(id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Student {id} not found")
