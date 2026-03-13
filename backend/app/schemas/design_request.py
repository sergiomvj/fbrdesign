from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.enums import DesignRequestStatus, RequestPriority, SourceSystem
from app.schemas.common import TimestampedSchema


class DesignRequestBase(BaseModel):
    brief_id: UUID
    project_id: UUID
    brand_id: UUID
    campaign_id: UUID | None = None
    source_system: SourceSystem
    source_reference_id: str | None = None
    request_type: str
    priority: RequestPriority
    status: DesignRequestStatus
    current_stage: str
    owner_team: str | None = None
    assigned_lead_name: str | None = None
    risk_level: str | None = None
    sla_due_at: datetime | None = None


class DesignRequestCreate(DesignRequestBase):
    pass


class DesignRequestUpdate(BaseModel):
    priority: RequestPriority | None = None
    status: DesignRequestStatus | None = None
    current_stage: str | None = None
    owner_team: str | None = None
    assigned_lead_name: str | None = None
    risk_level: str | None = None
    sla_due_at: datetime | None = None


class DesignRequestRead(DesignRequestBase, TimestampedSchema):
    id: UUID
    round_number: int
    requested_at: datetime
    approved_at: datetime | None = None
    delivered_at: datetime | None = None


class DesignRequestListResponse(BaseModel):
    data: list[DesignRequestRead]
    meta: dict[str, int]
    error: None = None


class DesignRequestCreateResponse(BaseModel):
    data: DesignRequestRead
    meta: dict[str, int | str]
    error: None = None
