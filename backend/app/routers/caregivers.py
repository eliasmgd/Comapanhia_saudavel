from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.deps import require_role
from app.models import CaregiverProfile, UserRole
from app.schemas import CaregiverProfileCreate, CaregiverProfileRead

router = APIRouter(prefix="/caregivers", tags=["caregivers"])


@router.post("/profile", response_model=CaregiverProfileRead, status_code=status.HTTP_201_CREATED)
def create_profile(
    payload: CaregiverProfileCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(UserRole.caregiver)),
):
    profile = db.query(CaregiverProfile).filter(CaregiverProfile.user_id == user.id).first()
    if profile:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Perfil já cadastrado")

    profile = CaregiverProfile(user_id=user.id, **payload.model_dump())
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


@router.get("", response_model=list[CaregiverProfileRead])
def list_approved_caregivers(db: Session = Depends(get_db)):
    return db.query(CaregiverProfile).filter(CaregiverProfile.approved.is_(True)).all()
