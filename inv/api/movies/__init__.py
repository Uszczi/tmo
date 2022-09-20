from inv.api.movies.movie import router
from inv.api.movies.create import router as r

router.include_router(r)
