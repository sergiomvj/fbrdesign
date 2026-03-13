export interface FeedbackEntry {
  id: string;
  thread_id: string;
  author_name: string;
  author_role?: string | null;
  message: string;
  is_change_request: boolean;
  created_at: string;
}

export interface FeedbackEntryListResponse {
  data: FeedbackEntry[];
  meta: { count: number };
  error: null;
}
