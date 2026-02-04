from fastapi import APIRouter

from app.api.router.jobs_router import jobs_router
from app.api.router.notifications_router import notifications_router

router = APIRouter()
router.include_router(jobs_router)
router.include_router(notifications_router)
