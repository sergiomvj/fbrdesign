from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.deliverable import Deliverable
from app.schemas.deliverable import (
    DeliverableCreate,
    DeliverableListResponse,
    DeliverableRead,
    DeliverableUpdate,
)

router = APIRouter(prefix="/deliverables", tags=["deliverables"])


@router.post("", response_model=DeliverableRead, status_code=status.HTTP_201_CREATED)
async def create_deliverable(
    payload: DeliverableCreate,
    db: AsyncSession = Depends(get_db),
) -> DeliverableRead:
    deliverable = Deliverable(**payload.model_dump())
    db.add(deliverable)
    await db.commit()
    await db.refresh(deliverable)
    return DeliverableRead.model_validate(deliverable)


@router.get("", response_model=DeliverableListResponse)
async def list_deliverables(
    design_request_id: UUID | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
) -> DeliverableListResponse:
    statement = select(Deliverable)
    if design_request_id is not None:
        statement = statement.where(Deliverable.design_request_id == design_request_id)
    result = await db.execute(statement)
    deliverables = result.scalars().all()
    return DeliverableListResponse(
        data=[DeliverableRead.model_validate(item) for item in deliverables],
        meta={"count": len(deliverables)},
        error=None,
    )


@router.patch("/{deliverable_id}", response_model=DeliverableRead)
async def update_deliverable(
    deliverable_id: UUID,
    payload: DeliverableUpdate,
    db: AsyncSession = Depends(get_db),
) -> DeliverableRead:
    result = await db.execute(select(Deliverable).where(Deliverable.id == deliverable_id))
    deliverable = result.scalar_one_or_none()
    if deliverable is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deliverable not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(deliverable, field, value)

    await db.commit()
    await db.refresh(deliverable)
    return DeliverableRead.model_validate(deliverable)
