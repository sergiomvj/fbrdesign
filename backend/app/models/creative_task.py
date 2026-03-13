from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.db_enum import enum_type
from app.models.enums import CreativeTaskStatus


class CreativeTask(Base):
    __tablename__ = "creative_tasks"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    design_request_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("design_requests.id"))
    parent_task_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("creative_tasks.id"))
    task_type: Mapped[str] = mapped_column(String(80), nullable=False)
    title: Mapped[str] = mapped_column(String(180), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    status: Mapped[CreativeTaskStatus] = mapped_column(enum_type(CreativeTaskStatus, "creative_task_status_enum"), nullable=False)
    assigned_to_name: Mapped[str | None] = mapped_column(String(150))
    depends_on_task_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("creative_tasks.id"))
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    due_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())