import requests

from app.core.config import settings
from app.core.logger import logger
from app.dtos.requests.programmer_publication_dto import TypePublication


def publier(publication_id: int, type_publication: TypePublication):
    ressource = (
        "actualites" if type_publication == TypePublication.ACTUALITE else "evenements"
    )
    url = f"{settings.NEXTJS_BASE_URL}/api/{ressource}/{publication_id}/publier"

    logger.info(f"[JOB EXEC] Début de publication : {ressource} ID {publication_id}")

    try:
        response = requests.post(url, timeout=10)
        response.raise_for_status()

        logger.info(
            f"[JOB EXEC] Publication réussie pour {ressource} {publication_id} (Status: {response.status_code})"
        )
    except Exception as e:
        logger.error(
            f"[JOB EXEC] Erreur critique publication {publication_id}: {str(e)}",
            exc_info=True,
        )


def archiver(publication_id: int, type_publication: TypePublication):
    ressource = (
        "actualites" if type_publication == TypePublication.ACTUALITE else "evenements"
    )
    url = f"{settings.NEXTJS_BASE_URL}/api/{ressource}/{publication_id}/archiver"

    try:
        response = requests.post(url, timeout=10)
        response.raise_for_status()

        logger.info(f"[JOB EXEC] Archivage terminé pour {ressource} {publication_id}")
    except Exception as e:
        logger.error(
            f"[JOB EXEC] Erreur lors de l'archivage {publication_id}: {e}",
            exc_info=True,
        )
