from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TimestampedSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime


class HealthResponse(BaseModel):
    status: str
    service: str
    environment: str


class ProjectRead(TimestampedSchema):
    id: UUID
    code: str
    name: str
