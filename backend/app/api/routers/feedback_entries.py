from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.feedback_entry import FeedbackEntry
from app.schemas.feedback_entry import FeedbackEntryCreate, FeedbackEntryListResponse, FeedbackEntryRead

router = APIRouter(prefix="/feedback-entries", tags=["feedback_entries"])


@router.post("", response_model=FeedbackEntryRead, status_code=status.HTTP_201_CREATED)
async def create_feedback_entry(payload: FeedbackEntryCreate, db: AsyncSession = Depends(get_db)) -> FeedbackEntryRead:
    entry = FeedbackEntry(**payload.model_dump())
    db.add(entry)
    await db.commit()
    await db.refresh(entry)
    return FeedbackEntryRead.model_validate(entry)


@router.get("", response_model=FeedbackEntryListResponse)
async def list_feedback_entries(thread_id: UUID | None = Query(default=None), db: AsyncSession = Depends(get_db)) -> FeedbackEntryListResponse:
    statement = select(FeedbackEntry)
    if thread_id is not None:
        statement = statement.where(FeedbackEntry.thread_id == thread_id)
    result = await db.execute(statement)
    entries = result.scalars().all()
    return FeedbackEntryListResponse(data=[FeedbackEntryRead.model_validate(item) for item in entries], meta={"count": len(entries)}, error=None)
