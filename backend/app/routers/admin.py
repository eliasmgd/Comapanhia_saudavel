from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.deps import require_role
from app.models import AuditLog, CareRequest, CaregiverProfile, UserRole
from app.schemas import CareRequestRead, CareRequestStatusUpdate

router = APIRouter(prefix="/admin", tags=["admin"])


@router.patch("/caregivers/{profile_id}/approve")
def approve_caregiver(profile_id: int, db: Session = Depends(get_db), user=Depends(require_role(UserRole.admin))):
    _ = user
    profile = db.query(CaregiverProfile).filter(CaregiverProfile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")

    profile.approved = True
    db.add(AuditLog(user_id=user.id, action="approve_caregiver", entity_type="caregiver_profile", entity_id=profile.id))
    db.commit()
    return {"message": "Cuidador aprovado"}


@router.patch("/requests/{request_id}/status", response_model=CareRequestRead)
def update_request_status(
    request_id: int,
    payload: CareRequestStatusUpdate,
    db: Session = Depends(get_db),
    user=Depends(require_role(UserRole.admin)),
):
    care_request = db.query(CareRequest).filter(CareRequest.id == request_id).first()
    if not care_request:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")

    care_request.status = payload.status
    db.add(AuditLog(user_id=user.id, action="update_request_status", entity_type="care_request", entity_id=care_request.id))
    db.commit()
    db.refresh(care_request)
    return care_request
