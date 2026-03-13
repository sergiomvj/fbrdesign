from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class FeedbackThread(Base):
    __tablename__ = "feedback_threads"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    target_type: Mapped[str] = mapped_column(String(40), nullable=False)
    target_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), nullable=False)
    design_request_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("design_requests.id"))
    status: Mapped[str] = mapped_column(String(30), default="open")
    title: Mapped[str | None] = mapped_column(String(180))
    created_by_name: Mapped[str] = mapped_column(String(150), nullable=False)
    latest_message: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
