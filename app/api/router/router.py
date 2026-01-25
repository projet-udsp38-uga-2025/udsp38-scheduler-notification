from fastapi import APIRouter

from app.api.router.jobs_router import router as jobs_router

router = APIRouter()
router.include_router(jobs_router)
