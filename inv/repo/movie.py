from datetime import date
from typing import Protocol

from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from inv.db import get_db
from inv.db.models.movie import MovieModel


class CreateMovie(Protocol):
    title: str
    watch_date: date
    production_year: str | None
    directors: str | None


class UpdateMovie(Protocol):
    title: str | None
    watch_date: date | None
    production_year: str | None
    directors: str | None

    def to_update(self) -> dict:
        return {}


class MovieRepo:
    @classmethod
    async def create(cls, movie: CreateMovie) -> MovieModel:
        data = {
            "title": movie.title,
            "watch_date": str(movie.watch_date),
            "production_year": movie.production_year,
            "directors": movie.directors,
        }

        db = get_db()

        new_movie = await db.movie.insert_one(data)
        cc = await db.movie.find_one({"_id": new_movie.inserted_id}, {"_id": 1})
        return cc["_id"]

    @classmethod
    async def create_many(cls, movies: list[CreateMovie]) -> MovieModel:
        data = [
            {
                "title": movie.title,
                "watch_date": str(movie.watch_date),
                "production_year": movie.production_year,
                "directors": movie.directors,
            }
            for movie in movies
        ]

        db = get_db()
        new_movie = await db.movie.insert_many(data)
        return new_movie

    @classmethod
    async def update(cls, id: str, movie: UpdateMovie):
        db = get_db()
        await db.movie.update_one(
            {"_id": ObjectId(id)}, {"$set": jsonable_encoder(movie.to_update())}
        )

    @classmethod
    def get(cls):
        pass
