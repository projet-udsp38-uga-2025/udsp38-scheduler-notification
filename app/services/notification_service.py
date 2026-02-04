from firebase_admin import messaging

from app.core.logger import logger
from app.dtos.requests.notifier_utilisateurs_dto import NotifierUtilisateursDTO


def notifier_utilisateurs(payload: NotifierUtilisateursDTO):
    logger.info(
        f"[FCM] Envoi d'un broadcast sur le topic '{payload.topic}' (Titre: {payload.titre})"
    )
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=payload.titre,
                body=payload.description,
            ),
            data=payload.data or {},
            topic=payload.topic,
        )

        message_id = messaging.send(message)
        logger.info(f"[FCM] Notification envoyé - id: '{message_id}'")
    except Exception as e:
        logger.error(
            f"[FCM] Échec de l'envoi sur '{payload.topic}': {e}", exc_info=True
        )
