from datetime import datetime

from pydantic import BaseModel, EmailStr

from app.models import CareRequestStatus, UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: UserRole
    lgpd_consent: bool = True


class UserRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: UserRole

    class Config:
        from_attributes = True


class LoginInput(BaseModel):
    email: EmailStr
    password: str


class CaregiverProfileCreate(BaseModel):
    experience_years: int
    specialties: str
    bio: str


class CaregiverProfileRead(BaseModel):
    id: int
    user: UserRead
    experience_years: int
    specialties: str
    bio: str
    approved: bool

    class Config:
        from_attributes = True


class CareRequestCreate(BaseModel):
    patient_name: str
    care_type: str
    details: str


class CareRequestRead(BaseModel):
    id: int
    requester_id: int
    patient_name: str
    care_type: str
    details: str
    status: CareRequestStatus
    created_at: datetime

    class Config:
        from_attributes = True


class CareRequestStatusUpdate(BaseModel):
    status: CareRequestStatus
