import requests

from app.core.config import settings
from app.dtos.requests.programmer_publication_dto import TypePublication


def publier(publication_id: int, type_publication: TypePublication):
    ressources_rest_api = {True: "actualites", False: "evenements"}[
        type_publication == TypePublication.ACTUALITE
    ]
    try:
        response = requests.post(
            f"{settings.NEXTJS_BASE_URL}/api/{ressources_rest_api}/{publication_id}/publier",
            timeout=5,
        )
        response.raise_for_status()
    except Exception as e:
        print(f"[Scheduler] Erreur publication {publication_id}: {e}")


def archiver(publication_id: int, type_publication: TypePublication):
    ressources_rest_api = {True: "actualites", False: "evenements"}[
        type_publication == TypePublication.ACTUALITE
    ]
    try:
        response = requests.post(
            f"{settings.NEXTJS_BASE_URL}/api/{ressources_rest_api}/{publication_id}/archiver",
            timeout=5,
        )
        response.raise_for_status()
    except Exception as e:
        print(f"[Scheduler] Erreur archivage {publication_id}: {e}")
