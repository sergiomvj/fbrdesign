from fastapi import FastAPI

from app.api.routers.approval_steps import router as approval_steps_router
from app.api.routers.asset_versions import router as asset_versions_router
from app.api.routers.briefs import router as briefs_router
from app.api.routers.creative_tasks import router as creative_tasks_router
from app.api.routers.deliverables import router as deliverables_router
from app.api.routers.design_requests import router as design_requests_router
from app.api.routers.feedback_entries import router as feedback_entries_router
from app.api.routers.feedback_threads import router as feedback_threads_router
from app.api.routers.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.app_debug,
    version="0.1.0",
)

app.include_router(health_router, prefix=settings.api_prefix)
app.include_router(briefs_router, prefix=settings.api_prefix)
app.include_router(design_requests_router, prefix=settings.api_prefix)
app.include_router(creative_tasks_router, prefix=settings.api_prefix)
app.include_router(deliverables_router, prefix=settings.api_prefix)
app.include_router(approval_steps_router, prefix=settings.api_prefix)
app.include_router(feedback_threads_router, prefix=settings.api_prefix)
app.include_router(feedback_entries_router, prefix=settings.api_prefix)
app.include_router(asset_versions_router, prefix=settings.api_prefix)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "status": "bootstrapped",
    }
