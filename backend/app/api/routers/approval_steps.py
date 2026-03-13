from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.approval_step import ApprovalStep
from app.schemas.approval_step import (
    ApprovalStepCreate,
    ApprovalStepListResponse,
    ApprovalStepRead,
    ApprovalStepUpdate,
)

router = APIRouter(prefix="/approval-steps", tags=["approval_steps"])


@router.post("", response_model=ApprovalStepRead, status_code=status.HTTP_201_CREATED)
async def create_approval_step(
    payload: ApprovalStepCreate,
    db: AsyncSession = Depends(get_db),
) -> ApprovalStepRead:
    approval_step = ApprovalStep(**payload.model_dump())
    db.add(approval_step)
    await db.commit()
    await db.refresh(approval_step)
    return ApprovalStepRead.model_validate(approval_step)


@router.get("", response_model=ApprovalStepListResponse)
async def list_approval_steps(
    design_request_id: UUID | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
) -> ApprovalStepListResponse:
    statement = select(ApprovalStep)
    if design_request_id is not None:
        statement = statement.where(ApprovalStep.design_request_id == design_request_id)
    result = await db.execute(statement)
    approval_steps = result.scalars().all()
    return ApprovalStepListResponse(
        data=[ApprovalStepRead.model_validate(item) for item in approval_steps],
        meta={"count": len(approval_steps)},
        error=None,
    )


@router.patch("/{approval_step_id}", response_model=ApprovalStepRead)
async def update_approval_step(
    approval_step_id: UUID,
    payload: ApprovalStepUpdate,
    db: AsyncSession = Depends(get_db),
) -> ApprovalStepRead:
    result = await db.execute(select(ApprovalStep).where(ApprovalStep.id == approval_step_id))
    approval_step = result.scalar_one_or_none()
    if approval_step is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Approval step not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(approval_step, field, value)

    await db.commit()
    await db.refresh(approval_step)
    return ApprovalStepRead.model_validate(approval_step)
