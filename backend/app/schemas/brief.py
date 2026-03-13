from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.enums import SourceSystem
from app.schemas.common import TimestampedSchema


class BriefBase(BaseModel):
    source_system: SourceSystem
    source_reference_id: str | None = None
    project_id: UUID
    brand_id: UUID
    campaign_id: UUID | None = None
    requester_name: str
    requester_email: EmailStr | None = None
    title: str
    objective: str
    audience: str | None = None
    channel: str | None = None
    constraints: str | None = None
    references_summary: str | None = None
    ai_intake_notes: str | None = None


class BriefCreate(BriefBase):
    pass


class BriefRead(BriefBase, TimestampedSchema):
    id: UUID


class BriefListResponse(BaseModel):
    data: list[BriefRead]
    meta: dict[str, int]
    error: None = None


class BriefCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    data: BriefRead
    meta: dict[str, int | str]
    error: None = None
