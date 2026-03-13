export type SourceSystem =
  | "fbr_sales"
  | "fbr_mkt"
  | "fbr_video"
  | "fbr_redacao"
  | "fbr_click"
  | "fbr_leads"
  | "fbr_finance"
  | "fbr_dev"
  | "internal_manual";

export interface Brief {
  id: string;
  source_system: SourceSystem;
  source_reference_id?: string | null;
  project_id: string;
  brand_id: string;
  campaign_id?: string | null;
  requester_name: string;
  requester_email?: string | null;
  title: string;
  objective: string;
  audience?: string | null;
  channel?: string | null;
  constraints?: string | null;
  references_summary?: string | null;
  ai_intake_notes?: string | null;
  created_at: string;
  updated_at: string;
}

export interface BriefCreateInput {
  source_system: SourceSystem;
  source_reference_id?: string | null;
  project_id: string;
  brand_id: string;
  campaign_id?: string | null;
  requester_name: string;
  requester_email?: string | null;
  title: string;
  objective: string;
  audience?: string | null;
  channel?: string | null;
  constraints?: string | null;
  references_summary?: string | null;
  ai_intake_notes?: string | null;
}

export interface BriefListResponse {
  data: Brief[];
  meta: {
    count: number;
    limit: number;
    offset: number;
  };
  error: null;
}

export interface BriefCreateResponse {
  data: Brief;
  meta: {
    count: number;
    [key: string]: number | string;
  };
  error: null;
}
