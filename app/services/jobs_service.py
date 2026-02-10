from apscheduler.job import Job
from apscheduler.triggers.date import DateTrigger

from app.core.config import TIMEZONE
from app.core.logger import logger
from app.core.scheduler import scheduler
from app.dtos.requests.archiver_publication_dto import ProgrammerArchivageRequestDTO
from app.dtos.requests.programmer_publication_dto import ProgrammerPublicationRequestDTO
from app.dtos.requests.supprimer_job_dto import SupprimerJobRequestDTO
from app.dtos.responses.job_programmation_dto import JobProgrammationDTO
from app.services.http_service import http_service


def programmer_publication(
    payload: ProgrammerPublicationRequestDTO,
) -> JobProgrammationDTO:
    job_id = f"publish_{payload.type_publication.name}_{payload.publication_id}"

    try:
        trigger = DateTrigger(run_date=payload.date_publication, timezone=TIMEZONE)
        job_publication: Job = scheduler.add_job(
            func=http_service.publier,
            trigger=trigger,
            args=[payload.publication_id, payload.type_publication],
            id=job_id,
            replace_existing=True,
            misfire_grace_time=3600,
        )

        logger.info(
            f"[Scheduler] Publication programmée pour {job_id} à {trigger.run_date} (Timezone: {TIMEZONE})"
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


def supprimer_job(supprimer_job_request: SupprimerJobRequestDTO) -> None:
    try:
        publish_job_id = f"publish_{supprimer_job_request.type_publication.name}_{supprimer_job_request.publication_id}"
        archive_job_id = f"archive_{supprimer_job_request.type_publication.name}_{supprimer_job_request.publication_id}"
        if scheduler.get_job(publish_job_id):
            scheduler.remove_job(publish_job_id)
        if scheduler.get_job(archive_job_id):
            scheduler.remove_job(archive_job_id)
    except Exception as e:
        logger.error(
            f"[Scheduler] Erreur lors de la suppression du job {supprimer_job_request.publication_id}: {e}",
            exc_info=True,
        )
        raise


def archiver_publication(
    payload: ProgrammerPublicationRequestDTO | ProgrammerArchivageRequestDTO,
) -> JobProgrammationDTO:
    if not payload.date_expiration:
        raise ValueError("Date expiration est requise pour l'archivage")

    job_id = f"archive_{payload.type_publication.name}_{payload.publication_id}"

    try:
        trigger = DateTrigger(run_date=payload.date_expiration, timezone=TIMEZONE)
        job = scheduler.add_job(
            func=http_service.archiver,
            trigger=trigger,
            args=[payload.publication_id, payload.type_publication],
            id=job_id,
            replace_existing=True,
            misfire_grace_time=3600,
        )

        logger.info(
            f"[Scheduler] Archivage programmé pour {job_id} à {trigger.run_date} (Timezone: {TIMEZONE})"
        )

        return JobProgrammationDTO(
            job_id=job.id,
            date_programmation=payload.date_expiration.isoformat(),
        )

    except Exception as e:
        logger.error(
            f"[Scheduler] Erreur lors de la planification de l'archivage pour {payload.publication_id}: {e}",
            exc_info=True,
        )
        raise
