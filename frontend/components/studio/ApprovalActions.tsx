"use client";

import { useMemo, useState, useTransition } from "react";
import type { CSSProperties } from "react";
import { useRouter } from "next/navigation";

import { StatusBadge } from "@/components/studio/StatusBadge";
import type { ApprovalStatus, ApprovalStep } from "@/types";

interface ApprovalActionsProps {
  designRequestId: string;
  initialRequestStatus: string;
  initialRequestStage: string;
  approvalSteps: ApprovalStep[];
}

export function ApprovalActions({
  designRequestId,
  initialRequestStatus,
  initialRequestStage,
  approvalSteps,
}: ApprovalActionsProps) {
  const router = useRouter();
  const [steps, setSteps] = useState(approvalSteps);
  const [requestStatus, setRequestStatus] = useState(initialRequestStatus);
  const [requestStage, setRequestStage] = useState(initialRequestStage);
  const [approverName, setApproverName] = useState("Creative Review Desk");
  const [decisionReason, setDecisionReason] = useState("");
  const [message, setMessage] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  const actionableSteps = useMemo(
    () => steps.filter((step) => step.status === "open" || step.status === "pending"),
    [steps],
  );

  function resolveRequestState(decision: ApprovalStatus, currentSteps: ApprovalStep[], updatedStepId: string) {
    if (decision === "changes_requested" || decision === "rejected") {
      return {
        status: "changes_requested",
        stage: "stakeholder_feedback",
      };
    }

    const nextSteps = currentSteps.map((step) =>
      step.id === updatedStepId ? { ...step, status: decision } : step,
    );
    const allApproved = nextSteps.every((step) => step.status === "approved" || step.status === "skipped");

    if (allApproved) {
      return {
        status: "approved",
        stage: "approved_for_delivery",
      };
    }

    return {
      status: "in_stakeholder_approval",
      stage: "approval_in_progress",
    };
  }

  function submitDecision(stepId: string, decision: ApprovalStatus) {
    setMessage(null);

    startTransition(async () => {
      const stepResponse = await fetch(`/api/approval-steps/${stepId}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          status: decision,
          approver_name: approverName || null,
          decision_reason: decisionReason || null,
        }),
      });

      if (!stepResponse.ok) {
        setMessage("Nao foi possivel registrar a decisao deste gate.");
        return;
      }

      const nextState = resolveRequestState(decision, steps, stepId);
      const requestResponse = await fetch(`/api/design-requests/${designRequestId}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          status: nextState.status,
          current_stage: nextState.stage,
        }),
      });

      if (!requestResponse.ok) {
        setMessage("Gate atualizado, mas a request nao refletiu o novo status.");
        return;
      }

      setSteps((current) =>
        current.map((step) =>
          step.id === stepId
            ? {
                ...step,
                status: decision,
                approver_name: approverName || step.approver_name,
                decision_reason: decisionReason || step.decision_reason,
                updated_at: new Date().toISOString(),
              }
            : step,
        ),
      );
      setRequestStatus(nextState.status);
      setRequestStage(nextState.stage);
      setDecisionReason("");
      setMessage(decision === "approved" ? "Aprovacao registrada." : "Pedido de ajustes registrado.");
      router.refresh();
    });
  }

  return (
    <div style={{ display: "grid", gap: 14 }}>
      <div style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "center" }}>
        <StatusBadge value={requestStatus} />
        <StatusBadge value={requestStage} />
      </div>

      <div style={{ display: "grid", gap: 12 }}>
        {steps.map((item) => (
          <div key={item.id} style={rowStyle}>
            <div style={{ display: "flex", justifyContent: "space-between", gap: 16 }}>
              <strong>{item.step_name}</strong>
              <StatusBadge value={item.status} />
            </div>
            <div style={{ color: "#c8d6eb" }}>
              Papel: {item.approver_role ?? "n/d"} • Responsavel: {item.approver_name ?? "n/d"}
            </div>
            {item.decision_reason ? <div style={{ color: "#c8d6eb" }}>Decisao: {item.decision_reason}</div> : null}
            {item.status === "open" || item.status === "pending" ? (
              <div style={{ display: "grid", gap: 10 }}>
                <input
                  value={approverName}
                  onChange={(event) => setApproverName(event.target.value)}
                  placeholder="Quem esta decidindo"
                  style={fieldStyle}
                />
                <textarea
                  value={decisionReason}
                  onChange={(event) => setDecisionReason(event.target.value)}
                  placeholder="Contexto da aprovacao ou pedido de ajustes"
                  style={{ ...fieldStyle, minHeight: 90, resize: "vertical" }}
                />
                <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
                  <button
                    type="button"
                    disabled={isPending}
                    onClick={() => submitDecision(item.id, "approved")}
                    style={{ ...buttonStyle, background: "#f97316", color: "#08111f" }}
                  >
                    Aprovar gate
                  </button>
                  <button
                    type="button"
                    disabled={isPending}
                    onClick={() => submitDecision(item.id, "changes_requested")}
                    style={{ ...buttonStyle, background: "transparent", color: "#eef4ff", border: "1px solid rgba(148,163,184,0.24)" }}
                  >
                    Pedir ajustes
                  </button>
                </div>
              </div>
            ) : null}
          </div>
        ))}
      </div>

      {actionableSteps.length === 0 ? (
        <p style={{ margin: 0, color: "#c8d6eb" }}>Todos os gates desta demanda ja receberam decisao.</p>
      ) : null}
      {message ? <p style={{ margin: 0, color: "#c8d6eb" }}>{message}</p> : null}
    </div>
  );
}

const rowStyle: CSSProperties = {
  display: "grid",
  gap: 8,
  paddingTop: 8,
  borderTop: "1px solid rgba(148,163,184,0.12)",
};

const fieldStyle: CSSProperties = {
  width: "100%",
  borderRadius: 14,
  border: "1px solid rgba(148,163,184,0.16)",
  background: "rgba(8,17,31,0.45)",
  color: "#eef4ff",
  padding: "12px 14px",
};

const buttonStyle: CSSProperties = {
  width: "fit-content",
  borderRadius: 999,
  padding: "10px 14px",
  fontWeight: 700,
  cursor: "pointer",
};
