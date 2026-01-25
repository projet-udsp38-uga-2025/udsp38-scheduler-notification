from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.alias_generators import to_camel

from app.core.config import FIREBASE_MAIN_TOPIC


class NotifierUtilisateursDTO(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    topic: str = FIREBASE_MAIN_TOPIC
    titre: str
    description: str
    data: dict | None = None

    @field_validator("data")
    @classmethod
    def cast_to_str(cls, v):
        return {k: str(val) for k, val in v.items()} if v else v
