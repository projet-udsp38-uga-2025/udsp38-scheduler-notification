import requests
from apscheduler.job import Job
from apscheduler.triggers.date import DateTrigger

from app.core.config import settings
from app.core.scheduler import scheduler
from app.dtos.requests.programmer_publication_dto import ProgrammerPublicationRequestDTO
from app.dtos.responses.job_programmation_dto import JobProgrammationDTO


def publier(article_id: int):
    try:
        response = requests.post(
            f"{settings.NEXTJS_BASE_URL}/api/actualites/publier/{article_id}", timeout=5
        )
        response.raise_for_status()
    except Exception as e:
        print(f"[Scheduler] Erreur publication {article_id}: {e}")


async def programmer_publication(
    payload: ProgrammerPublicationRequestDTO,
) -> JobProgrammationDTO:
    trigger = DateTrigger(run_date=payload.date_programmation, timezone="Europe/Paris")

    job: Job = scheduler.add_job(
        func=publier,
        trigger=trigger,
        args=[payload.publication_id],
        replace_existing=True,
    )

    return JobProgrammationDTO(
        job_id=job.id, date_programmation=payload.date_programmation.isoformat()
    )


def supprimer_job(job_id: str) -> dict:
    scheduler.remove_job(job_id)
    return {"jobId": job_id, "status": "deleted"}
