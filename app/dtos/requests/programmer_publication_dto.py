from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class TypePublication(Enum):
    ACTUALITE = "actualite"
    EVENEMENT = "evenement"


class ProgrammerPublicationRequestDTO(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )

    publication_id: int
    type_publication: TypePublication
    date_publication: datetime
    date_expiration: datetime | None = None
