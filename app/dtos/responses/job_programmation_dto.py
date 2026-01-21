from pydantic import BaseModel


class JobProgrammationDTO(BaseModel):
    job_id: str
    date_programmation: str
