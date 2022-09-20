from fastapi import APIRouter

from inv.api.movies.create import router as create_router
from inv.api.movies.movie import router as movie_router

router = APIRouter(tags=["Movies"])

router.include_router(movie_router)
router.include_router(create_router)
