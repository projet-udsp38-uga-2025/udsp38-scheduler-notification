from fastapi import APIRouter

from app.dtos.requests.archiver_publication_dto import ProgrammerArchivageRequestDTO
from app.dtos.requests.programmer_publication_dto import ProgrammerPublicationRequestDTO
from app.dtos.requests.supprimer_job_dto import SupprimerJobRequestDTO
from app.dtos.responses.job_programmation_dto import JobProgrammationDTO
from app.services.jobs_service import (
    archiver_publication,
    programmer_publication,
    supprimer_job as service_supprimer_job,
)

jobs_router = APIRouter(prefix="/jobs", tags=["jobs"])


@jobs_router.post("/programmer-publication", response_model=JobProgrammationDTO)
async def programmer(payload: ProgrammerPublicationRequestDTO):
    return programmer_publication(payload)

@jobs_router.post("/programmer-archivage", response_model=JobProgrammationDTO)
async def archiver(payload: ProgrammerArchivageRequestDTO):
    return archiver_publication(payload)

@jobs_router.delete("/supprimer-job")
async def supprimer_job(payload: SupprimerJobRequestDTO):
    return service_supprimer_job(payload)