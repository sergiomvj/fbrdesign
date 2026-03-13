export type CreativeTaskStatus =
  | "pending"
  | "ready"
  | "in_progress"
  | "blocked"
  | "in_review"
  | "done"
  | "cancelled";

export interface CreativeTask {
  id: string;
  design_request_id: string;
  parent_task_id?: string | null;
  task_type: string;
  title: string;
  description?: string | null;
  status: CreativeTaskStatus;
  assigned_to_name?: string | null;
  depends_on_task_id?: string | null;
  started_at?: string | null;
  due_at?: string | null;
  completed_at?: string | null;
  created_at: string;
  updated_at: string;
}

export interface CreativeTaskListResponse {
  data: CreativeTask[];
  meta: { count: number };
  error: null;
}
