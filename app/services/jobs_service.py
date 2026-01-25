from apscheduler.job import Job
from apscheduler.triggers.date import DateTrigger

from app.core.config import TIMEZONE
from app.core.scheduler import scheduler
from app.dtos.requests.programmer_publication_dto import ProgrammerPublicationRequestDTO
from app.dtos.responses.job_programmation_dto import JobProgrammationDTO
from app.services.http_service import archiver, publier


def programmer_publication(
    payload: ProgrammerPublicationRequestDTO,
) -> JobProgrammationDTO:
    trigger = DateTrigger(run_date=payload.date_publication, timezone=TIMEZONE)
    job_publication: Job = scheduler.add_job(
        func=publier,
        trigger=trigger,
        args=[payload.publication_id, payload.type_publication],
        replace_existing=True,
    )

    if payload.date_expiration is not None:
        archiver_publication(payload)

    return JobProgrammationDTO(
        job_id=job_publication.id,
        date_programmation=payload.date_publication.isoformat(),
    )


def archiver_publication(payload: ProgrammerPublicationRequestDTO) -> None:
    trigger = DateTrigger(run_date=payload.date_expiration, timezone=TIMEZONE)
    scheduler.add_job(
        func=archiver,
        trigger=trigger,
        args=[payload.publication_id],
        replace_existing=True,
    )
