from bson import ObjectId

from inv.db import get_db
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
        movies = await db["movie"].find().sort([("watch_date", -1)]).to_list(1000)
        return movies

    # @classmethod
    # TODO
    # async def delete(cls, id: str) -> None:
    #     db = get_db()
    #     delete_result = await db["movie"].delete_one({"_id": ObjectId(id)})
    #     return delete_result
