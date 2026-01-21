from fastapi import FastAPI
from app.core.scheduler import scheduler
from app.api.router import router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan, title="Scheduler Service")

app.include_router(router, prefix="/api/v1")
