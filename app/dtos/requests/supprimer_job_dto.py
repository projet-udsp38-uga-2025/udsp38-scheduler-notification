from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from app.dtos.requests.programmer_publication_dto import TypePublication

class SupprimerJobRequestDTO(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )
    publication_id: int
    type_publication: TypePublication