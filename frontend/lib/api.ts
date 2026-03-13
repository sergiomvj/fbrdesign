import { STUDIO_DEFAULTS } from "@/lib/studio-defaults";
import type {
  ApprovalStep,
  ApprovalStepListResponse,
  AssetVersion,
  AssetVersionListResponse,
  Brief,
  BriefListResponse,
  CreativeTask,
  CreativeTaskListResponse,
  Deliverable,
  DeliverableListResponse,
  DesignRequest,
  DesignRequestListResponse,
  FeedbackEntry,
  FeedbackEntryListResponse,
  FeedbackThread,
  FeedbackThreadListResponse,
} from "@/types";

const now = () => new Date().toISOString();

const mockBriefs: Brief[] = [
  {
    id: "10000000-0000-0000-0000-000000000001",
    source_system: "fbr_sales",
    source_reference_id: "sales-campaign-128",
    project_id: STUDIO_DEFAULTS.projectId,
    brand_id: STUDIO_DEFAULTS.brandId,
    campaign_id: STUDIO_DEFAULTS.campaignId,
    requester_name: "Ana Lima",
    requester_email: "ana@fbr.com",
    title: "Media kit institucional 2026",
    objective: "Atualizar material comercial da unidade.",
    audience: "Parceiros e anunciantes",
    channel: "commercial",
    constraints: "Usar linguagem institucional e assets aprovados.",
    references_summary: "Basear no kit do ano passado e na campanha atual.",
    ai_intake_notes: null,
    created_at: now(),
    updated_at: now(),
  },
];

const mockDesignRequests: DesignRequest[] = [
  {
    id: "20000000-0000-0000-0000-000000000001",
    brief_id: mockBriefs[0].id,
    project_id: STUDIO_DEFAULTS.projectId,
    brand_id: STUDIO_DEFAULTS.brandId,
    campaign_id: STUDIO_DEFAULTS.campaignId,
    source_system: "fbr_sales",
    source_reference_id: "sales-campaign-128",
    request_type: "media_kit",
    priority: "high",
    status: "in_stakeholder_approval",
    current_stage: "commercial_review",
    owner_team: "design",
    assigned_lead_name: "Studio Core",
    risk_level: "medium",
    sla_due_at: new Date(Date.now() + 86400000).toISOString(),
    round_number: 2,
    requested_at: now(),
    approved_at: null,
    delivered_at: null,
    created_at: now(),
    updated_at: now(),
  },
];

const mockCreativeTasks: CreativeTask[] = [
  {
    id: "30000000-0000-0000-0000-000000000001",
    design_request_id: mockDesignRequests[0].id,
    task_type: "layout",
    title: "Montar segunda versao do media kit",
    description: "Refinar bloco comercial e atualizar capa.",
    status: "in_review",
    assigned_to_name: "Studio Core",
    parent_task_id: null,
    depends_on_task_id: null,
    started_at: now(),
    due_at: new Date(Date.now() + 21600000).toISOString(),
    completed_at: null,
    created_at: now(),
    updated_at: now(),
  },
];

const mockDeliverables: Deliverable[] = [
  {
    id: "40000000-0000-0000-0000-000000000001",
    design_request_id: mockDesignRequests[0].id,
    deliverable_type: "media_kit",
    name: "Media Kit 2026",
    format: "pdf",
    channel: "commercial",
    status: "approval_pending",
    delivery_channel: "fbr_sales",
    final_version_id: "90000000-0000-0000-0000-000000000002",
    approved_at: null,
    delivered_at: null,
    created_at: now(),
    updated_at: now(),
  },
];

const mockApprovalSteps: ApprovalStep[] = [
  {
    id: "50000000-0000-0000-0000-000000000001",
    target_type: "deliverable",
    target_id: mockDeliverables[0].id,
    design_request_id: mockDesignRequests[0].id,
    deliverable_id: mockDeliverables[0].id,
    step_order: 1,
    step_name: "Aprovacao comercial",
    approver_role: "sales_manager",
    approver_name: "Carlos Sales",
    status: "open",
    decision_reason: null,
    due_at: new Date(Date.now() + 43200000).toISOString(),
    decided_at: null,
    created_at: now(),
    updated_at: now(),
  },
];

const mockFeedbackThreads: FeedbackThread[] = [
  {
    id: "60000000-0000-0000-0000-000000000001",
    target_type: "deliverable",
    target_id: mockDeliverables[0].id,
    design_request_id: mockDesignRequests[0].id,
    status: "open",
    title: "Ajustes no bloco comercial",
    created_by_name: "Carlos Sales",
    latest_message: "Reforcar os bundles premium na pagina 3.",
    created_at: now(),
    updated_at: now(),
  },
];

const mockFeedbackEntries: FeedbackEntry[] = [
  {
    id: "70000000-0000-0000-0000-000000000001",
    thread_id: mockFeedbackThreads[0].id,
    author_name: "Carlos Sales",
    author_role: "sales_manager",
    message: "Reforcar os bundles premium na pagina 3.",
    is_change_request: true,
    created_at: now(),
  },
];

const mockAssetVersions: AssetVersion[] = [
  {
    id: "90000000-0000-0000-0000-000000000001",
    asset_file_id: "80000000-0000-0000-0000-000000000001",
    version_number: 1,
    derived_from_version_id: null,
    storage_key: "brands/facebrasil/media-kit-v1.pdf",
    storage_bucket: "fbr-design-assets",
    mime_type: "application/pdf",
    file_size_bytes: 1820332,
    checksum: "sha256-v1",
    origin_type: "designer_upload",
    change_summary: "Primeira proposta comercial",
    is_final: false,
    approved_by_name: null,
    approved_at: null,
    created_at: now(),
  },
  {
    id: "90000000-0000-0000-0000-000000000002",
    asset_file_id: "80000000-0000-0000-0000-000000000001",
    version_number: 2,
    derived_from_version_id: "90000000-0000-0000-0000-000000000001",
    storage_key: "brands/facebrasil/media-kit-v2.pdf",
    storage_bucket: "fbr-design-assets",
    mime_type: "application/pdf",
    file_size_bytes: 1955442,
    checksum: "sha256-v2",
    origin_type: "designer_upload",
    change_summary: "Ajuste comercial e refinamento de capa",
    is_final: true,
    approved_by_name: "Carlos Sales",
    approved_at: now(),
    created_at: now(),
  },
];

async function parseJson<T>(response: Response): Promise<T> {
  if (!response.ok) throw new Error(`Request failed with status ${response.status}`);
  return (await response.json()) as T;
}

export async function getBriefs(): Promise<BriefListResponse> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) {
    return {
      data: mockBriefs,
      meta: { count: mockBriefs.length, limit: mockBriefs.length, offset: 0 },
      error: null,
    };
  }
  return parseJson<BriefListResponse>(await fetch(`${backendUrl}/api/briefs`, { cache: "no-store" }));
}

export async function getDesignRequests(): Promise<DesignRequestListResponse> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) {
    return {
      data: mockDesignRequests,
      meta: { count: mockDesignRequests.length, limit: mockDesignRequests.length, offset: 0 },
      error: null,
    };
  }
  return parseJson<DesignRequestListResponse>(await fetch(`${backendUrl}/api/design-requests`, { cache: "no-store" }));
}

export async function getDesignRequestById(id: string): Promise<DesignRequest | null> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) return mockDesignRequests.find((item) => item.id === id) ?? null;
  const response = await fetch(`${backendUrl}/api/design-requests/${id}`, { cache: "no-store" });
  if (response.status === 404) return null;
  return parseJson<DesignRequest>(response);
}

export async function getCreativeTasks(designRequestId?: string): Promise<CreativeTaskListResponse> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) {
    const filtered = designRequestId ? mockCreativeTasks.filter((item) => item.design_request_id === designRequestId) : mockCreativeTasks;
    return { data: filtered, meta: { count: filtered.length }, error: null };
  }
  const url = new URL(`${backendUrl}/api/creative-tasks`);
  if (designRequestId) url.searchParams.set("design_request_id", designRequestId);
  return parseJson<CreativeTaskListResponse>(await fetch(url, { cache: "no-store" }));
}

export async function getDeliverables(designRequestId?: string): Promise<DeliverableListResponse> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) {
    const filtered = designRequestId ? mockDeliverables.filter((item) => item.design_request_id === designRequestId) : mockDeliverables;
    return { data: filtered, meta: { count: filtered.length }, error: null };
  }
  const url = new URL(`${backendUrl}/api/deliverables`);
  if (designRequestId) url.searchParams.set("design_request_id", designRequestId);
  return parseJson<DeliverableListResponse>(await fetch(url, { cache: "no-store" }));
}

export async function getApprovalSteps(designRequestId?: string): Promise<ApprovalStepListResponse> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) {
    const filtered = designRequestId ? mockApprovalSteps.filter((item) => item.design_request_id === designRequestId) : mockApprovalSteps;
    return { data: filtered, meta: { count: filtered.length }, error: null };
  }
  const url = new URL(`${backendUrl}/api/approval-steps`);
  if (designRequestId) url.searchParams.set("design_request_id", designRequestId);
  return parseJson<ApprovalStepListResponse>(await fetch(url, { cache: "no-store" }));
}

export async function getFeedbackThreads(designRequestId?: string): Promise<FeedbackThreadListResponse> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) {
    const filtered = designRequestId ? mockFeedbackThreads.filter((item) => item.design_request_id === designRequestId) : mockFeedbackThreads;
    return { data: filtered, meta: { count: filtered.length }, error: null };
  }
  const url = new URL(`${backendUrl}/api/feedback-threads`);
  if (designRequestId) url.searchParams.set("design_request_id", designRequestId);
  return parseJson<FeedbackThreadListResponse>(await fetch(url, { cache: "no-store" }));
}

export async function getFeedbackEntries(threadId?: string): Promise<FeedbackEntryListResponse> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) {
    const filtered = threadId ? mockFeedbackEntries.filter((item) => item.thread_id === threadId) : mockFeedbackEntries;
    return { data: filtered, meta: { count: filtered.length }, error: null };
  }
  const url = new URL(`${backendUrl}/api/feedback-entries`);
  if (threadId) url.searchParams.set("thread_id", threadId);
  return parseJson<FeedbackEntryListResponse>(await fetch(url, { cache: "no-store" }));
}

export async function getAssetVersions(): Promise<AssetVersionListResponse> {
  const backendUrl = process.env.FBR_DESIGN_API_URL;
  if (!backendUrl) return { data: mockAssetVersions, meta: { count: mockAssetVersions.length }, error: null };
  return parseJson<AssetVersionListResponse>(await fetch(`${backendUrl}/api/asset-versions`, { cache: "no-store" }));
}

export async function getRequestDetail(id: string) {
  const [request, briefs, creativeTasks, deliverables, approvalSteps, feedbackThreads, assetVersions] = await Promise.all([
    getDesignRequestById(id),
    getBriefs(),
    getCreativeTasks(id),
    getDeliverables(id),
    getApprovalSteps(id),
    getFeedbackThreads(id),
    getAssetVersions(),
  ]);

  if (!request) return null;

  const brief = briefs.data.find((item) => item.id === request.brief_id) ?? null;
  const threadIds = feedbackThreads.data.map((item) => item.id);
  const feedbackEntries = (await Promise.all(threadIds.map((threadId) => getFeedbackEntries(threadId)))).flatMap((item) => item.data);
  const relevantVersions = assetVersions.data.filter((item) => deliverables.data.some((deliverable) => deliverable.final_version_id === item.id));

  return {
    request,
    brief,
    creativeTasks: creativeTasks.data,
    deliverables: deliverables.data,
    approvalSteps: approvalSteps.data,
    feedbackThreads: feedbackThreads.data,
    feedbackEntries,
    assetVersions: relevantVersions,
  };
}
