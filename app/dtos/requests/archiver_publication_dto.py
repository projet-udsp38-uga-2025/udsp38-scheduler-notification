from datetime import datetime
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from app.dtos.requests.programmer_publication_dto import TypePublication

class ProgrammerArchivageRequestDTO(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )

    publication_id: int
    date_expiration: datetime
    type_publication: TypePublication