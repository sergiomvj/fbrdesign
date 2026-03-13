from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.enums import DeliverableStatus, DeliverableType


class Deliverable(Base):
    __tablename__ = "deliverables"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    design_request_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("design_requests.id"))
    deliverable_type: Mapped[DeliverableType]
    name: Mapped[str] = mapped_column(String(180), nullable=False)
    format: Mapped[str] = mapped_column(String(60), nullable=False)
    channel: Mapped[str | None] = mapped_column(String(120))
    status: Mapped[DeliverableStatus]
    delivery_channel: Mapped[str | None] = mapped_column(String(120))
    final_version_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True))
    approved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    delivered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
