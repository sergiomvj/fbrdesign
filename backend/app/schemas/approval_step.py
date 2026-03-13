from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.enums import ApprovalStatus
from app.schemas.common import TimestampedSchema


class ApprovalStepBase(BaseModel):
    target_type: str
    target_id: UUID
    design_request_id: UUID
    deliverable_id: UUID | None = None
    step_order: int
    step_name: str
    approver_role: str | None = None
    approver_name: str | None = None
    status: ApprovalStatus
    decision_reason: str | None = None
    due_at: datetime | None = None


class ApprovalStepCreate(ApprovalStepBase):
    pass


class ApprovalStepUpdate(BaseModel):
    status: ApprovalStatus | None = None
    approver_name: str | None = None
    decision_reason: str | None = None
    due_at: datetime | None = None


class ApprovalStepRead(ApprovalStepBase, TimestampedSchema):
    id: UUID
    decided_at: datetime | None = None


class ApprovalStepListResponse(BaseModel):
    data: list[ApprovalStepRead]
    meta: dict[str, int]
    error: None = None
