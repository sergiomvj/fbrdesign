from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.db_enum import enum_type
from app.models.enums import DesignRequestStatus, RequestPriority, SourceSystem


class DesignRequest(Base):
    __tablename__ = "design_requests"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    brief_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("briefs.id"))
    project_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("projects.id"))
    brand_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("brands.id"))
    campaign_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("campaigns.id"))
    source_system: Mapped[SourceSystem] = mapped_column(enum_type(SourceSystem, "source_system_enum"), nullable=False)
    source_reference_id: Mapped[str | None] = mapped_column(String(120))
    request_type: Mapped[str] = mapped_column(String(80), nullable=False)
    priority: Mapped[RequestPriority] = mapped_column(enum_type(RequestPriority, "request_priority_enum"), nullable=False)
    status: Mapped[DesignRequestStatus] = mapped_column(enum_type(DesignRequestStatus, "design_request_status_enum"), nullable=False)
    current_stage: Mapped[str] = mapped_column(String(80), nullable=False)
    round_number: Mapped[int] = mapped_column(default=1)
    owner_team: Mapped[str | None] = mapped_column(String(80))
    assigned_lead_name: Mapped[str | None] = mapped_column(String(150))
    risk_level: Mapped[str | None] = mapped_column(String(30))
    sla_due_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    requested_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    approved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    delivered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )