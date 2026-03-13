from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.asset_version import AssetVersion
from app.schemas.asset_version import (
    AssetVersionCreate,
    AssetVersionListResponse,
    AssetVersionRead,
    AssetVersionUpdate,
)

router = APIRouter(prefix="/asset-versions", tags=["asset_versions"])


@router.post("", response_model=AssetVersionRead, status_code=status.HTTP_201_CREATED)
async def create_asset_version(
    payload: AssetVersionCreate,
    db: AsyncSession = Depends(get_db),
) -> AssetVersionRead:
    version = AssetVersion(**payload.model_dump())
    db.add(version)
    await db.commit()
    await db.refresh(version)
    return AssetVersionRead.model_validate(version)


@router.get("", response_model=AssetVersionListResponse)
async def list_asset_versions(
    asset_file_id: UUID | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
) -> AssetVersionListResponse:
    statement = select(AssetVersion)
    if asset_file_id is not None:
        statement = statement.where(AssetVersion.asset_file_id == asset_file_id)
    result = await db.execute(statement)
    versions = result.scalars().all()
    return AssetVersionListResponse(
        data=[AssetVersionRead.model_validate(item) for item in versions],
        meta={"count": len(versions)},
        error=None,
    )


@router.patch("/{version_id}", response_model=AssetVersionRead)
async def update_asset_version(
    version_id: UUID,
    payload: AssetVersionUpdate,
    db: AsyncSession = Depends(get_db),
) -> AssetVersionRead:
    result = await db.execute(select(AssetVersion).where(AssetVersion.id == version_id))
    version = result.scalar_one_or_none()
    if version is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asset version not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(version, field, value)

    await db.commit()
    await db.refresh(version)
    return AssetVersionRead.model_validate(version)
