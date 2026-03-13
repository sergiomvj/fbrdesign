from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class FeedbackEntryBase(BaseModel):
    thread_id: UUID
    author_name: str
    author_role: str | None = None
    message: str
    is_change_request: bool = False


class FeedbackEntryCreate(FeedbackEntryBase):
    pass


class FeedbackEntryRead(FeedbackEntryBase):
    id: UUID
    created_at: datetime


class FeedbackEntryListResponse(BaseModel):
    data: list[FeedbackEntryRead]
    meta: dict[str, int]
    error: None = None
