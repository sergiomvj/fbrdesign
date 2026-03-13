import Link from "next/link";

import { StatusBadge } from "@/components/studio/StatusBadge";
import { getApprovalSteps, getDesignRequests } from "@/lib/api";

export default async function ReviewsPage() {
  const [requestsPayload, approvalsPayload] = await Promise.all([getDesignRequests(), getApprovalSteps()]);
  const actionableApprovals = approvalsPayload.data.filter((item) => item.status === "open" || item.status === "pending");

  return (
    <section style={{ display: "grid", gap: 18 }}>
      <div>
        <p style={{ color: "#f97316", textTransform: "uppercase", letterSpacing: "0.18em", fontSize: 12 }}>
          Review & Approval
        </p>
        <h1 style={{ fontSize: 40, marginBottom: 12 }}>Inbox de aprovacoes</h1>
        <p style={{ color: "#c8d6eb", maxWidth: 720 }}>
          A central de revisao agora ja nasce orientada por approval steps reais do dominio, em vez de depender apenas
          do status agregado da request.
        </p>
      </div>

      <div style={{ display: "grid", gap: 16 }}>
        {actionableApprovals.map((approval) => {
          const request = requestsPayload.data.find((item) => item.id === approval.design_request_id);

          return (
            <Link
              key={approval.id}
              href={`/requests/${approval.design_request_id}`}
              style={{
                display: "grid",
                gap: 10,
                padding: 18,
                border: "1px solid rgba(148,163,184,0.16)",
                borderRadius: 18,
                background: "rgba(20,31,49,0.45)",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", gap: 16, alignItems: "center" }}>
                <strong style={{ fontSize: 22 }}>{approval.step_name}</strong>
                <StatusBadge value={approval.status} />
              </div>
              <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
                <StatusBadge value={request?.status ?? "request_missing"} />
                <StatusBadge value={request?.priority ?? "n/a"} />
              </div>
              <p style={{ color: "#c8d6eb", margin: 0 }}>
                Request: {request?.request_type ?? "nao encontrada"} • Papel: {approval.approver_role ?? "n/d"}
              </p>
            </Link>
          );
        })}
      </div>
    </section>
  );
}
