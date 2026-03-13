from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class AssetVersion(Base):
    __tablename__ = "asset_versions"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    asset_file_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("asset_files.id"))
    version_number: Mapped[int] = mapped_column(Integer, nullable=False)
    derived_from_version_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("asset_versions.id"))
    storage_key: Mapped[str] = mapped_column(String(255), nullable=False)
    storage_bucket: Mapped[str] = mapped_column(String(120), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(120), nullable=False)
    file_size_bytes: Mapped[int] = mapped_column(BigInteger, nullable=False)
    checksum: Mapped[str] = mapped_column(String(128), nullable=False)
    origin_type: Mapped[str] = mapped_column(String(60), nullable=False)
    change_summary: Mapped[str | None] = mapped_column(Text)
    is_final: Mapped[bool] = mapped_column(Boolean, default=False)
    approved_by_name: Mapped[str | None] = mapped_column(String(150))
    approved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
