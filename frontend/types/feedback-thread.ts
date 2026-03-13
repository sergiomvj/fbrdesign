export interface FeedbackThread {
  id: string;
  target_type: string;
  target_id: string;
  design_request_id: string;
  status: string;
  title?: string | null;
  created_by_name: string;
  latest_message?: string | null;
  created_at: string;
  updated_at: string;
}

export interface FeedbackThreadListResponse {
  data: FeedbackThread[];
  meta: { count: number };
  error: null;
}
