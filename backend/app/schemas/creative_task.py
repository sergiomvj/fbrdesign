from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.enums import CreativeTaskStatus
from app.schemas.common import TimestampedSchema


class CreativeTaskBase(BaseModel):
    design_request_id: UUID
    parent_task_id: UUID | None = None
    task_type: str
    title: str
    description: str | None = None
    status: CreativeTaskStatus
    assigned_to_name: str | None = None
    depends_on_task_id: UUID | None = None
    started_at: datetime | None = None
    due_at: datetime | None = None
    completed_at: datetime | None = None


class CreativeTaskCreate(CreativeTaskBase):
    pass


class CreativeTaskUpdate(BaseModel):
    status: CreativeTaskStatus | None = None
    assigned_to_name: str | None = None
    due_at: datetime | None = None
    completed_at: datetime | None = None


class CreativeTaskRead(CreativeTaskBase, TimestampedSchema):
    id: UUID


class CreativeTaskListResponse(BaseModel):
    data: list[CreativeTaskRead]
    meta: dict[str, int]
    error: None = None
