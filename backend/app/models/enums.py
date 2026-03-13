from enum import Enum


class SourceSystem(str, Enum):
    FBR_SALES = "fbr_sales"
    FBR_MKT = "fbr_mkt"
    FBR_VIDEO = "fbr_video"
    FBR_REDACAO = "fbr_redacao"
    FBR_CLICK = "fbr_click"
    FBR_LEADS = "fbr_leads"
    FBR_FINANCE = "fbr_finance"
    FBR_DEV = "fbr_dev"
    INTERNAL_MANUAL = "internal_manual"


class RequestPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class DesignRequestStatus(str, Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    TRIAGED = "triaged"
    QUEUED = "queued"
    IN_PRODUCTION = "in_production"
    IN_INTERNAL_REVIEW = "in_internal_review"
    IN_STAKEHOLDER_APPROVAL = "in_stakeholder_approval"
    CHANGES_REQUESTED = "changes_requested"
    APPROVED = "approved"
    DELIVERED = "delivered"
    ARCHIVED = "archived"
    CANCELLED = "cancelled"


class DeliverableStatus(str, Enum):
    NOT_STARTED = "not_started"
    DRAFT_READY = "draft_ready"
    REVIEW_READY = "review_ready"
    APPROVAL_PENDING = "approval_pending"
    APPROVED = "approved"
    DELIVERED = "delivered"
    SUPERSEDED = "superseded"


class DeliverableType(str, Enum):
    SOCIAL_POST = "social_post"
    BANNER = "banner"
    PRESENTATION = "presentation"
    MEDIA_KIT = "media_kit"
    BRAND_ASSET = "brand_asset"
    INSTITUTIONAL_PIECE = "institutional_piece"
    THUMBNAIL = "thumbnail"
    CAMPAIGN_KIT = "campaign_kit"
    EDITORIAL_PIECE = "editorial_piece"


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    OPEN = "open"
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"
    REJECTED = "rejected"
    SKIPPED = "skipped"
