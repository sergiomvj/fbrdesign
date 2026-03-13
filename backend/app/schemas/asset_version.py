from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AssetVersionBase(BaseModel):
    asset_file_id: UUID
    version_number: int
    derived_from_version_id: UUID | None = None
    storage_key: str
    storage_bucket: str
    mime_type: str
    file_size_bytes: int
    checksum: str
    origin_type: str
    change_summary: str | None = None
    is_final: bool = False
    approved_by_name: str | None = None
    approved_at: datetime | None = None


class AssetVersionCreate(AssetVersionBase):
    pass


class AssetVersionUpdate(BaseModel):
    change_summary: str | None = None
    is_final: bool | None = None
    approved_by_name: str | None = None
    approved_at: datetime | None = None


class AssetVersionRead(AssetVersionBase):
    id: UUID
    created_at: datetime


class AssetVersionListResponse(BaseModel):
    data: list[AssetVersionRead]
    meta: dict[str, int]
    error: None = None
