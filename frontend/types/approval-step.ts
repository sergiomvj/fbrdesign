export type ApprovalStatus =
  | "pending"
  | "open"
  | "approved"
  | "changes_requested"
  | "rejected"
  | "skipped";

export interface ApprovalStep {
  id: string;
  target_type: string;
  target_id: string;
  design_request_id: string;
  deliverable_id?: string | null;
  step_order: number;
  step_name: string;
  approver_role?: string | null;
  approver_name?: string | null;
  status: ApprovalStatus;
  decision_reason?: string | null;
  due_at?: string | null;
  decided_at?: string | null;
  created_at: string;
  updated_at: string;
}

export interface ApprovalStepCreateInput {
  target_type: string;
  target_id: string;
  design_request_id: string;
  deliverable_id?: string | null;
  step_order: number;
  step_name: string;
  approver_role?: string | null;
  approver_name?: string | null;
  status: ApprovalStatus;
  decision_reason?: string | null;
  due_at?: string | null;
}

export interface ApprovalStepUpdateInput {
  status?: ApprovalStatus;
  approver_name?: string | null;
  decision_reason?: string | null;
  due_at?: string | null;
}

export interface ApprovalStepListResponse {
  data: ApprovalStep[];
  meta: { count: number };
  error: null;
}
