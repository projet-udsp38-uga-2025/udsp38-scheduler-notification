from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler

from app.core.config import settings

jobstores = {"default": SQLAlchemyJobStore(url=settings.DATABASE_URL)}

scheduler = BackgroundScheduler(jobstores=jobstores, timezone="Europe/Paris")
