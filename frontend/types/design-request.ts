import type { SourceSystem } from "./brief";

export type RequestPriority = "low" | "medium" | "high" | "urgent";

export type DesignRequestStatus =
  | "draft"
  | "submitted"
  | "triaged"
  | "queued"
  | "in_production"
  | "in_internal_review"
  | "in_stakeholder_approval"
  | "changes_requested"
  | "approved"
  | "delivered"
  | "archived"
  | "cancelled";

export interface DesignRequest {
  id: string;
  brief_id: string;
  project_id: string;
  brand_id: string;
  campaign_id?: string | null;
  source_system: SourceSystem;
  source_reference_id?: string | null;
  request_type: string;
  priority: RequestPriority;
  status: DesignRequestStatus;
  current_stage: string;
  owner_team?: string | null;
  assigned_lead_name?: string | null;
  risk_level?: string | null;
  sla_due_at?: string | null;
  round_number: number;
  requested_at: string;
  approved_at?: string | null;
  delivered_at?: string | null;
  created_at: string;
  updated_at: string;
}

export interface DesignRequestCreateInput {
  brief_id: string;
  project_id: string;
  brand_id: string;
  campaign_id?: string | null;
  source_system: SourceSystem;
  source_reference_id?: string | null;
  request_type: string;
  priority: RequestPriority;
  status: DesignRequestStatus;
  current_stage: string;
  owner_team?: string | null;
  assigned_lead_name?: string | null;
  risk_level?: string | null;
  sla_due_at?: string | null;
}

export interface DesignRequestUpdateInput {
  priority?: RequestPriority;
  status?: DesignRequestStatus;
  current_stage?: string;
  owner_team?: string | null;
  assigned_lead_name?: string | null;
  risk_level?: string | null;
  sla_due_at?: string | null;
}

export interface DesignRequestListResponse {
  data: DesignRequest[];
  meta: {
    count: number;
    limit: number;
    offset: number;
  };
  error: null;
}

export interface DesignRequestCreateResponse {
  data: DesignRequest;
  meta: {
    count: number;
    [key: string]: number | string;
  };
  error: null;
}
