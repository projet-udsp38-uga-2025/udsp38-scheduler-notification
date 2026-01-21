from fastapi import APIRouter

from app.dtos.requests.programmer_publication_dto import ProgrammerPublicationRequestDTO
from app.dtos.responses.job_programmation_dto import JobProgrammationDTO
from app.services.jobs_service import programmer_publication

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("/programmer-publication", response_model=JobProgrammationDTO)
async def programmer(payload: ProgrammerPublicationRequestDTO):
    return await programmer_publication(payload)
