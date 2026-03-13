from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.schemas.common import TimestampedSchema


class FeedbackThreadBase(BaseModel):
    target_type: str
    target_id: UUID
    design_request_id: UUID
    status: str = "open"
    title: str | None = None
    created_by_name: str
    latest_message: str | None = None


class FeedbackThreadCreate(FeedbackThreadBase):
    pass


class FeedbackThreadUpdate(BaseModel):
    status: str | None = None
    latest_message: str | None = None


class FeedbackThreadRead(FeedbackThreadBase, TimestampedSchema):
    id: UUID


class FeedbackThreadListResponse(BaseModel):
    data: list[FeedbackThreadRead]
    meta: dict[str, int]
    error: None = None
