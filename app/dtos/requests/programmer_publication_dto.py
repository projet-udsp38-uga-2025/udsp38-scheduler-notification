from datetime import datetime

from pydantic import BaseModel


class ProgrammerPublicationRequestDTO(BaseModel):
    publication_id: int
    date_programmation: datetime
