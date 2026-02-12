from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.deps import require_role
from app.models import CareRequest, UserRole
from app.schemas import CareRequestCreate, CareRequestRead

router = APIRouter(prefix="/requests", tags=["care-requests"])


@router.post("", response_model=CareRequestRead, status_code=status.HTTP_201_CREATED)
def create_request(
    payload: CareRequestCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(UserRole.requester)),
):
    care_request = CareRequest(requester_id=user.id, **payload.model_dump())
    db.add(care_request)
    db.commit()
    db.refresh(care_request)
    return care_request


@router.get("/my", response_model=list[CareRequestRead])
def list_my_requests(db: Session = Depends(get_db), user=Depends(require_role(UserRole.requester))):
    return db.query(CareRequest).filter(CareRequest.requester_id == user.id).all()


@router.get("", response_model=list[CareRequestRead])
def list_all_requests(db: Session = Depends(get_db), user=Depends(require_role(UserRole.admin))):
    _ = user
    return db.query(CareRequest).all()
