from fastapi import APIRouter

from app.dtos.requests.programmer_publication_dto import ProgrammerPublicationRequestDTO
from app.dtos.responses.job_programmation_dto import JobProgrammationDTO
from app.services.jobs_service import programmer_publication

jobs_router = APIRouter(prefix="/jobs", tags=["jobs"])


@jobs_router.post("/programmer-publication", response_model=JobProgrammationDTO)
async def programmer(payload: ProgrammerPublicationRequestDTO):
    return programmer_publication(payload)
