from fastapi import APIRouter, Depends, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.brief import Brief
from app.schemas.brief import BriefCreate, BriefCreateResponse, BriefListResponse, BriefRead

router = APIRouter(prefix="/briefs", tags=["briefs"])


@router.post("", response_model=BriefCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_brief(payload: BriefCreate, db: AsyncSession = Depends(get_db)) -> BriefCreateResponse:
    brief = Brief(**payload.model_dump())
    db.add(brief)
    await db.commit()
    await db.refresh(brief)
    return BriefCreateResponse(data=BriefRead.model_validate(brief), meta={"count": 1}, error=None)


@router.get("", response_model=BriefListResponse)
async def list_briefs(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
) -> BriefListResponse:
    result = await db.execute(select(Brief).offset(offset).limit(limit))
    briefs = result.scalars().all()
    return BriefListResponse(
        data=[BriefRead.model_validate(item) for item in briefs],
        meta={"count": len(briefs), "limit": limit, "offset": offset},
        error=None,
    )
