from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, List
from inv.db import get_db

from inv.shared.models import PyObjectId

from fastapi import APIRouter

router = APIRouter(tags=["movies"])

db = get_db()


class UpdateMovieModel(BaseModel):
    title: Optional[str]
    published_year: Optional[str]
    watch_date: Optional[str]
    directors: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        son_encoders = {ObjectId: str}

        schema_extra = {
            "example": {
                "title": "TODO",
                "published": "TODO",
                "watch_date": "TOOD",
                "directors": "TOOD",
            }
        }


class MovieModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str | None = None
    production_year: str | None = None
    watch_date: str | None = None
    directors: str | None = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

        schema_extra = {
            "example": {
                "title": "TODO",
                "published": "TODO",
                "watch_date": "TOOD",
                "directors": "TOOD",
            }
        }


@router.post("/movie", response_model=MovieModel)
async def create_movie(student: MovieModel = Body(...)):
    student = jsonable_encoder(student)
    new_student = await db["students"].insert_one(student)
    created_student = await db["students"].find_one({"_id": new_student.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)


@router.get("/movies", response_model=List[MovieModel])
async def list_movies():
    students = await db["students"].find().to_list(1000)
    return students


@router.delete("/movie/{id}")
async def delete_movie(id: str):
    delete_result = await db["students"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@router.get(
    "/movie/{id}",
    response_model=MovieModel,
)
async def show_movie(id: str):
    if (student := await db["students"].find_one({"_id": id})) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@router.put("/movie/{id}", response_model=MovieModel)
async def update_movie(id: str, student: UpdateMovieModel = Body(...)):
    student = {k: v for k, v in student.dict().items() if v is not None}

    if len(student) >= 1:
        update_result = await db["students"].update_one({"_id": id}, {"$set": student})

        if update_result.modified_count == 1:
            if (
                updated_student := await db["students"].find_one({"_id": id})
            ) is not None:
                return updated_student

    if (existing_student := await db["students"].find_one({"_id": id})) is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")
