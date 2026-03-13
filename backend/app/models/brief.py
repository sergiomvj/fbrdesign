from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.enums import SourceSystem


class Brief(Base):
    __tablename__ = "briefs"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    source_system: Mapped[SourceSystem]
    source_reference_id: Mapped[str | None] = mapped_column(String(120))
    project_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("projects.id"))
    brand_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("brands.id"))
    campaign_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("campaigns.id"))
    requester_name: Mapped[str] = mapped_column(String(150), nullable=False)
    requester_email: Mapped[str | None] = mapped_column(String(180))
    title: Mapped[str] = mapped_column(String(180), nullable=False)
    objective: Mapped[str] = mapped_column(Text, nullable=False)
    audience: Mapped[str | None] = mapped_column(Text)
    channel: Mapped[str | None] = mapped_column(String(120))
    constraints: Mapped[str | None] = mapped_column(Text)
    references_summary: Mapped[str | None] = mapped_column(Text)
    ai_intake_notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
