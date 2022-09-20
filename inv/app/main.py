from fastapi import FastAPI
from inv.api.movies import router as movies_router
from inv.api.books import router as books_router
from fastapi import APIRouter

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api")
router.include_router(movies_router)
router.include_router(books_router)

app.include_router(router)
