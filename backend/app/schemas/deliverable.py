from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.enums import DeliverableStatus, DeliverableType
from app.schemas.common import TimestampedSchema


class DeliverableBase(BaseModel):
    design_request_id: UUID
    deliverable_type: DeliverableType
    name: str
    format: str
    channel: str | None = None
    status: DeliverableStatus
    delivery_channel: str | None = None
    final_version_id: UUID | None = None


class DeliverableCreate(DeliverableBase):
    pass


class DeliverableUpdate(BaseModel):
    status: DeliverableStatus | None = None
    delivery_channel: str | None = None
    final_version_id: UUID | None = None


class DeliverableRead(DeliverableBase, TimestampedSchema):
    id: UUID
    approved_at: datetime | None = None
    delivered_at: datetime | None = None


class DeliverableListResponse(BaseModel):
    data: list[DeliverableRead]
    meta: dict[str, int]
    error: None = None
