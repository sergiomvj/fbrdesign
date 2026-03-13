from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.design_request import DesignRequest
from app.schemas.design_request import (
    DesignRequestCreate,
    DesignRequestCreateResponse,
    DesignRequestListResponse,
    DesignRequestRead,
    DesignRequestUpdate,
)

router = APIRouter(prefix="/design-requests", tags=["design_requests"])


@router.post("", response_model=DesignRequestCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_design_request(
    payload: DesignRequestCreate,
    db: AsyncSession = Depends(get_db),
) -> DesignRequestCreateResponse:
    request = DesignRequest(**payload.model_dump())
    db.add(request)
    await db.commit()
    await db.refresh(request)
    return DesignRequestCreateResponse(
        data=DesignRequestRead.model_validate(request),
        meta={"count": 1},
        error=None,
    )


@router.get("", response_model=DesignRequestListResponse)
async def list_design_requests(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
) -> DesignRequestListResponse:
    result = await db.execute(select(DesignRequest).offset(offset).limit(limit))
    requests = result.scalars().all()
    return DesignRequestListResponse(
        data=[DesignRequestRead.model_validate(item) for item in requests],
        meta={"count": len(requests), "limit": limit, "offset": offset},
        error=None,
    )


@router.get("/{request_id}", response_model=DesignRequestRead)
async def get_design_request(request_id: UUID, db: AsyncSession = Depends(get_db)) -> DesignRequestRead:
    result = await db.execute(select(DesignRequest).where(DesignRequest.id == request_id))
    request = result.scalar_one_or_none()
    if request is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Design request not found")
    return DesignRequestRead.model_validate(request)


@router.patch("/{request_id}", response_model=DesignRequestRead)
async def update_design_request(
    request_id: UUID,
    payload: DesignRequestUpdate,
    db: AsyncSession = Depends(get_db),
) -> DesignRequestRead:
    result = await db.execute(select(DesignRequest).where(DesignRequest.id == request_id))
    request = result.scalar_one_or_none()
    if request is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Design request not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(request, field, value)

    await db.commit()
    await db.refresh(request)
    return DesignRequestRead.model_validate(request)
