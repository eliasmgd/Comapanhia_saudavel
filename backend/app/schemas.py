from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from .models import ApprovalStatus, CareRequestStatus, UserRole


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: UserRole
    oauth_provider: str = Field(examples=["google", "facebook", "instagram"])


class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole

    class Config:
        from_attributes = True


class CaregiverCreate(BaseModel):
    user_id: int
    specialties: str
    bio: str
    city: str


class CaregiverRead(BaseModel):
    id: int
    user_id: int
    specialties: str
    bio: str
    city: str
    approval_status: ApprovalStatus

    class Config:
        from_attributes = True


class CareRequestCreate(BaseModel):
    requester_id: int
    patient_name: str
    location: str
    details: str


class CareRequestRead(BaseModel):
    id: int
    requester_id: int
    patient_name: str
    location: str
    details: str
    status: CareRequestStatus
    created_at: datetime

    class Config:
        from_attributes = True


class StatusUpdate(BaseModel):
    status: CareRequestStatus


class ApprovalUpdate(BaseModel):
    approval_status: ApprovalStatus
