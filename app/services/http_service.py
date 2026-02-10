import requests

from app.core.config import settings
from app.core.logger import logger
from app.dtos.requests.programmer_publication_dto import TypePublication


class HttpService:
    def __init__(self):
        self.base_url = f"{settings.PORTAIL_BASE_URL}/api"
        self.session = requests.Session()

        self.session.headers.update(
            {"X-Api-Key": settings.PORTAIL_API_KEY, "Content-Type": "application/json"}
        )

    def _get_ressource_name(self, type_publication: TypePublication) -> str:
        """Détermine le segment d'URL en fonction du type de publication."""
        return (
            "actualites"
            if type_publication == TypePublication.ACTUALITE
            else "evenements"
        )

    def publier(self, publication_id: int, type_publication: TypePublication):
        ressource = self._get_ressource_name(type_publication)
        url = f"{self.base_url}/{ressource}/{publication_id}/publier"

        logger.info(
            f"[JOB EXEC] Début de publication : {ressource} ID {publication_id}"
        )

        try:
            response = self.session.post(url, timeout=10)
            response.raise_for_status()

            logger.info(
                f"[JOB EXEC] Publication réussie pour {ressource} {publication_id} (Status: {response.status_code})"
            )
        except requests.exceptions.RequestException as e:
            logger.error(
                f"[JOB EXEC] Erreur critique publication {publication_id}: {str(e)}",
                exc_info=True,
            )

    def archiver(self, publication_id: int, type_publication: TypePublication):
        ressource = self._get_ressource_name(type_publication)
        url = f"{self.base_url}/{ressource}/{publication_id}/archiver"

        try:
            response = self.session.post(url, timeout=10)
            response.raise_for_status()

            logger.info(
                f"[JOB EXEC] Archivage terminé pour {ressource} {publication_id}"
            )
        except requests.exceptions.RequestException as e:
            logger.error(
                f"[JOB EXEC] Erreur lors de l'archivage {publication_id}: {e}",
                exc_info=True,
            )


http_service = HttpService()
