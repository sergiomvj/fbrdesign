from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.feedback_thread import FeedbackThread
from app.schemas.feedback_thread import (
    FeedbackThreadCreate,
    FeedbackThreadListResponse,
    FeedbackThreadRead,
    FeedbackThreadUpdate,
)

router = APIRouter(prefix="/feedback-threads", tags=["feedback_threads"])


@router.post("", response_model=FeedbackThreadRead, status_code=status.HTTP_201_CREATED)
async def create_feedback_thread(
    payload: FeedbackThreadCreate,
    db: AsyncSession = Depends(get_db),
) -> FeedbackThreadRead:
    thread = FeedbackThread(**payload.model_dump())
    db.add(thread)
    await db.commit()
    await db.refresh(thread)
    return FeedbackThreadRead.model_validate(thread)


@router.get("", response_model=FeedbackThreadListResponse)
async def list_feedback_threads(
    design_request_id: UUID | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
) -> FeedbackThreadListResponse:
    statement = select(FeedbackThread)
    if design_request_id is not None:
        statement = statement.where(FeedbackThread.design_request_id == design_request_id)
    result = await db.execute(statement)
    threads = result.scalars().all()
    return FeedbackThreadListResponse(
        data=[FeedbackThreadRead.model_validate(item) for item in threads],
        meta={"count": len(threads)},
        error=None,
    )


@router.patch("/{thread_id}", response_model=FeedbackThreadRead)
async def update_feedback_thread(
    thread_id: UUID,
    payload: FeedbackThreadUpdate,
    db: AsyncSession = Depends(get_db),
) -> FeedbackThreadRead:
    result = await db.execute(select(FeedbackThread).where(FeedbackThread.id == thread_id))
    thread = result.scalar_one_or_none()
    if thread is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Feedback thread not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(thread, field, value)

    await db.commit()
    await db.refresh(thread)
    return FeedbackThreadRead.model_validate(thread)
