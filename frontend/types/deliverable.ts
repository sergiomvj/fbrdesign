export type DeliverableStatus =
  | "not_started"
  | "draft_ready"
  | "review_ready"
  | "approval_pending"
  | "approved"
  | "delivered"
  | "superseded";

export type DeliverableType =
  | "social_post"
  | "banner"
  | "presentation"
  | "media_kit"
  | "brand_asset"
  | "institutional_piece"
  | "thumbnail"
  | "campaign_kit"
  | "editorial_piece";

export interface Deliverable {
  id: string;
  design_request_id: string;
  deliverable_type: DeliverableType;
  name: string;
  format: string;
  channel?: string | null;
  status: DeliverableStatus;
  delivery_channel?: string | null;
  final_version_id?: string | null;
  approved_at?: string | null;
  delivered_at?: string | null;
  created_at: string;
  updated_at: string;
}

export interface DeliverableListResponse {
  data: Deliverable[];
  meta: { count: number };
  error: null;
}
