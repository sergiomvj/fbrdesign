from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.creative_task import CreativeTask
from app.schemas.creative_task import CreativeTaskCreate, CreativeTaskListResponse, CreativeTaskRead, CreativeTaskUpdate

router = APIRouter(prefix="/creative-tasks", tags=["creative_tasks"])


@router.post("", response_model=CreativeTaskRead, status_code=status.HTTP_201_CREATED)
async def create_creative_task(payload: CreativeTaskCreate, db: AsyncSession = Depends(get_db)) -> CreativeTaskRead:
    task = CreativeTask(**payload.model_dump())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return CreativeTaskRead.model_validate(task)


@router.get("", response_model=CreativeTaskListResponse)
async def list_creative_tasks(
    design_request_id: UUID | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
) -> CreativeTaskListResponse:
    statement = select(CreativeTask)
    if design_request_id is not None:
        statement = statement.where(CreativeTask.design_request_id == design_request_id)
    result = await db.execute(statement)
    tasks = result.scalars().all()
    return CreativeTaskListResponse(data=[CreativeTaskRead.model_validate(item) for item in tasks], meta={"count": len(tasks)}, error=None)


@router.patch("/{task_id}", response_model=CreativeTaskRead)
async def update_creative_task(task_id: UUID, payload: CreativeTaskUpdate, db: AsyncSession = Depends(get_db)) -> CreativeTaskRead:
    result = await db.execute(select(CreativeTask).where(CreativeTask.id == task_id))
    task = result.scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Creative task not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    await db.commit()
    await db.refresh(task)
    return CreativeTaskRead.model_validate(task)
