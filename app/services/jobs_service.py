from apscheduler.job import Job
from apscheduler.triggers.date import DateTrigger

from app.core.config import TIMEZONE
from app.core.logger import logger
from app.core.scheduler import scheduler
from app.dtos.requests.programmer_publication_dto import ProgrammerPublicationRequestDTO
from app.dtos.responses.job_programmation_dto import JobProgrammationDTO
from app.services.http_service import archiver, publier


def programmer_publication(
    payload: ProgrammerPublicationRequestDTO,
) -> JobProgrammationDTO:
    logger.info(
        f"[Scheduler] Programmation d'une publication (ID: {payload.publication_id}, "
        f"Type: {payload.type_publication}) pour le {payload.date_publication}"
    )

    try:
        trigger = DateTrigger(run_date=payload.date_publication, timezone=TIMEZONE)
        job_publication: Job = scheduler.add_job(
            func=publier,
            trigger=trigger,
            args=[payload.publication_id, payload.type_publication],
            replace_existing=True,
        )

        logger.info(
            f"[Scheduler] Job de publication créé avec succès (Job ID: {job_publication.id})"
        )

        if payload.date_expiration is not None:
            archiver_publication(payload)

        return JobProgrammationDTO(
            job_id=job_publication.id,
            date_programmation=payload.date_publication.isoformat(),
        )
    except Exception as e:
        logger.error(
            f"[Scheduler] Erreur lors de la programmation de la publication {payload.publication_id}: {e}",
            exc_info=True,
        )
        raise


def archiver_publication(payload: ProgrammerPublicationRequestDTO) -> None:
    logger.info(
        f"[Scheduler] Planification de l'archivage pour {payload.publication_id} au {payload.date_expiration}"
    )
    try:
        trigger = DateTrigger(run_date=payload.date_expiration, timezone=TIMEZONE)
        job_archive: Job = scheduler.add_job(
            func=archiver,
            trigger=trigger,
            args=[payload.publication_id, payload.type_publication],
            replace_existing=True,
        )
        logger.info(f"[Scheduler] Job d'archivage créé (Job ID: {job_archive.id})")

    except Exception as e:
        logger.error(
            f"[Scheduler] Erreur lors de la planification de l'archivage pour {payload.publication_id}: {e}",
            exc_info=True,
        )
