from inv.db import get_db
from bson import ObjectId

from inv.db.models.movie import MovieModel


class MovieQuery:
    @classmethod
    async def get(cls, id: str) -> MovieModel:
        db = get_db()
        result = await db["movie"].find_one({"_id": ObjectId(id)})

        if not result:
            # TODO
            raise Exception

        return MovieModel(**result)

    @classmethod
    async def get_all(cls) -> list[MovieModel]:
        db = get_db()
        movies = await db["students"].find().to_list(1000)
        return movies

    @classmethod
    async def delete(cls, id: str) -> None:
        db = get_db()
        delete_result = await db["students"].delete_one({"_id": ObjectId(id)})
        return delete_result
