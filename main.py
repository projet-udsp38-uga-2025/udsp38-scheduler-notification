from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router.router import router
from app.core.scheduler import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan, title="Scheduler Service")

app.include_router(router, prefix="/api")
