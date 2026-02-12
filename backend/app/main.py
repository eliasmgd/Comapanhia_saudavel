from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import AuditLog, CareRequest, CareRequestStatus, Caregiver, User, UserRole
from .schemas import (
    ApprovalUpdate,
    CareRequestCreate,
    CareRequestRead,
    CaregiverCreate,
    CaregiverRead,
    StatusUpdate,
    UserCreate,
    UserRead,
)

app = FastAPI(title="Companhia Saudável API", version="0.1.0")


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/auth/social", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def social_login(payload: UserCreate, db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.email == payload.email).first()
    if user:
        return user

    user = User(**payload.model_dump())
    db.add(user)
    db.add(AuditLog(action="social_login_register", target="user", actor_id=None))
    db.commit()
    db.refresh(user)
    return user


@app.post("/caregivers", response_model=CaregiverRead, status_code=status.HTTP_201_CREATED)
def create_caregiver(payload: CaregiverCreate, db: Session = Depends(get_db)) -> Caregiver:
    user = db.get(User, payload.user_id)
    if not user or user.role != UserRole.CAREGIVER:
        raise HTTPException(status_code=400, detail="Usuário cuidador inválido")

    caregiver = Caregiver(**payload.model_dump())
    db.add(caregiver)
    db.add(AuditLog(action="caregiver_profile_created", target="caregiver", actor_id=user.id))
    db.commit()
    db.refresh(caregiver)
    return caregiver


@app.get("/caregivers", response_model=list[CaregiverRead])
def list_caregivers(db: Session = Depends(get_db)) -> list[Caregiver]:
    return db.query(Caregiver).all()


@app.post("/care-requests", response_model=CareRequestRead, status_code=status.HTTP_201_CREATED)
def create_request(payload: CareRequestCreate, db: Session = Depends(get_db)) -> CareRequest:
    user = db.get(User, payload.requester_id)
    if not user or user.role != UserRole.REQUESTER:
        raise HTTPException(status_code=400, detail="Solicitante inválido")

    request = CareRequest(**payload.model_dump())
    db.add(request)
    db.add(AuditLog(action="care_request_created", target="care_request", actor_id=user.id))
    db.commit()
    db.refresh(request)
    return request


@app.get("/care-requests", response_model=list[CareRequestRead])
def list_requests(db: Session = Depends(get_db)) -> list[CareRequest]:
    return db.query(CareRequest).all()


@app.patch("/care-requests/{request_id}", response_model=CareRequestRead)
def update_request_status(
    request_id: int,
    payload: StatusUpdate,
    db: Session = Depends(get_db),
) -> CareRequest:
    request = db.get(CareRequest, request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")

    request.status = payload.status
    db.add(AuditLog(action="care_request_status_updated", target=f"care_request:{request_id}"))
    db.commit()
    db.refresh(request)
    return request


@app.patch("/admin/caregivers/{caregiver_id}", response_model=CaregiverRead)
def approve_caregiver(
    caregiver_id: int,
    payload: ApprovalUpdate,
    db: Session = Depends(get_db),
) -> Caregiver:
    caregiver = db.get(Caregiver, caregiver_id)
    if not caregiver:
        raise HTTPException(status_code=404, detail="Cuidador não encontrado")

    caregiver.approval_status = payload.approval_status
    db.add(AuditLog(action="caregiver_approval_updated", target=f"caregiver:{caregiver_id}"))
    db.commit()
    db.refresh(caregiver)
    return caregiver


@app.get("/admin/dashboard")
def admin_dashboard(db: Session = Depends(get_db)) -> dict[str, int]:
    return {
        "users": db.query(User).count(),
        "caregivers": db.query(Caregiver).count(),
        "open_requests": db.query(CareRequest).filter(CareRequest.status == CareRequestStatus.OPEN).count(),
        "audit_logs": db.query(AuditLog).count(),
    }
