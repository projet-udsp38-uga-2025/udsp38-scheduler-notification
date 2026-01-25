from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.dtos.requests.notifier_utilisateurs_dto import NotifierUtilisateursDTO
from app.services.notification_service import notifier_utilisateurs

notifications_router = APIRouter(prefix="/notifications", tags=["notifications"])


@notifications_router.post("/", response_model=None)
async def notifier_fcm(
    payload: NotifierUtilisateursDTO, background_tasks: BackgroundTasks
):
    try:
        background_tasks.add_task(notifier_utilisateurs, payload)
        return {"message": "Notification en cours d'envoi"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur de préparation: {e}")
