import type { ReactNode } from "react";
import { notFound } from "next/navigation";

import { ApprovalActions } from "@/components/studio/ApprovalActions";
import { StatusBadge } from "@/components/studio/StatusBadge";
import { getRequestDetail } from "@/lib/api";

function Card({ children }: { children: ReactNode }) {
  return (
    <div
      style={{
        display: "grid",
        gap: 12,
        padding: 20,
        borderRadius: 18,
        border: "1px solid rgba(148,163,184,0.16)",
        background: "rgba(20,31,49,0.45)",
      }}
    >
      {children}
    </div>
  );
}

export default async function RequestDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const detail = await getRequestDetail(id);

  if (!detail) notFound();

  const { request, brief, creativeTasks, deliverables, approvalSteps, feedbackThreads, feedbackEntries, assetVersions } = detail;

  return (
    <section style={{ display: "grid", gap: 18 }}>
      <div>
        <p style={{ color: "#f97316", textTransform: "uppercase", letterSpacing: "0.18em", fontSize: 12 }}>
          Request Detail
        </p>
        <h1 style={{ fontSize: 44, marginBottom: 10 }}>{request.request_type}</h1>
        <p style={{ color: "#c8d6eb", maxWidth: 760 }}>
          Tela mestra inicial com briefing, tasks, deliverables, gates, feedbacks e versoes. Esta tela agora ja aceita
          decisao operacional nos approval gates e prepara o caminho para a timeline completa.
        </p>
      </div>

      <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
        <StatusBadge value={request.status} />
        <StatusBadge value={request.priority} />
        <StatusBadge value={request.current_stage} />
      </div>

      <div style={{ display: "grid", gap: 16, gridTemplateColumns: "1.2fr 0.8fr" }}>
        <Card>
          <strong style={{ fontSize: 22 }}>Resumo da demanda</strong>
          <div>Origem: {request.source_system}</div>
          <div>Responsavel: {request.assigned_lead_name ?? "n/d"}</div>
          <div>Squad: {request.owner_team ?? "n/d"}</div>
          <div>Risco: {request.risk_level ?? "n/d"}</div>
          <div>Rodada atual: {request.round_number}</div>
          <div>SLA: {request.sla_due_at ?? "n/d"}</div>
        </Card>

        <Card>
          <strong style={{ fontSize: 22 }}>Briefing</strong>
          <div>Titulo: {brief?.title ?? "n/d"}</div>
          <div>Solicitante: {brief?.requester_name ?? "n/d"}</div>
          <div>Canal: {brief?.channel ?? "n/d"}</div>
          <div>Objetivo: {brief?.objective ?? "n/d"}</div>
        </Card>
      </div>

      <Card>
        <strong style={{ fontSize: 22 }}>Creative Tasks</strong>
        <div style={{ display: "grid", gap: 12 }}>
          {creativeTasks.map((item) => (
            <div key={item.id} style={{ display: "grid", gap: 8, paddingTop: 8, borderTop: "1px solid rgba(148,163,184,0.12)" }}>
              <div style={{ display: "flex", justifyContent: "space-between", gap: 16 }}>
                <strong>{item.title}</strong>
                <StatusBadge value={item.status} />
              </div>
              <div style={{ color: "#c8d6eb" }}>
                Tipo: {item.task_type} • Responsavel: {item.assigned_to_name ?? "n/d"}
              </div>
            </div>
          ))}
        </div>
      </Card>

      <Card>
        <strong style={{ fontSize: 22 }}>Deliverables</strong>
        <div style={{ display: "grid", gap: 12 }}>
          {deliverables.map((item) => (
            <div key={item.id} style={{ display: "grid", gap: 8, paddingTop: 8, borderTop: "1px solid rgba(148,163,184,0.12)" }}>
              <div style={{ display: "flex", justifyContent: "space-between", gap: 16 }}>
                <strong>{item.name}</strong>
                <StatusBadge value={item.status} />
              </div>
              <div style={{ color: "#c8d6eb" }}>
                Tipo: {item.deliverable_type} • Formato: {item.format} • Canal: {item.channel ?? "n/d"}
              </div>
            </div>
          ))}
        </div>
      </Card>

      <div style={{ display: "grid", gap: 16, gridTemplateColumns: "1fr 1fr" }}>
        <Card>
          <strong style={{ fontSize: 22 }}>Approval Gates</strong>
          <ApprovalActions
            designRequestId={request.id}
            initialRequestStatus={request.status}
            initialRequestStage={request.current_stage}
            approvalSteps={approvalSteps}
          />
        </Card>

        <Card>
          <strong style={{ fontSize: 22 }}>Feedback Threads</strong>
          <div style={{ display: "grid", gap: 12 }}>
            {feedbackThreads.map((item) => (
              <div key={item.id} style={{ display: "grid", gap: 8, paddingTop: 8, borderTop: "1px solid rgba(148,163,184,0.12)" }}>
                <strong>{item.title ?? "Feedback"}</strong>
                <div style={{ color: "#c8d6eb" }}>Por: {item.created_by_name}</div>
                <div style={{ color: "#c8d6eb" }}>{item.latest_message ?? "Sem mensagem"}</div>
              </div>
            ))}
          </div>
        </Card>
      </div>

      <Card>
        <strong style={{ fontSize: 22 }}>Feedback Entries</strong>
        <div style={{ display: "grid", gap: 12 }}>
          {feedbackEntries.map((item) => (
            <div key={item.id} style={{ display: "grid", gap: 8, paddingTop: 8, borderTop: "1px solid rgba(148,163,184,0.12)" }}>
              <div style={{ display: "flex", justifyContent: "space-between", gap: 16 }}>
                <strong>{item.author_name}</strong>
                <StatusBadge value={item.is_change_request ? "change_request" : "comment"} />
              </div>
              <div style={{ color: "#c8d6eb" }}>{item.message}</div>
            </div>
          ))}
        </div>
      </Card>

      <Card>
        <strong style={{ fontSize: 22 }}>Versions</strong>
        <div style={{ display: "grid", gap: 12 }}>
          {assetVersions.map((item) => (
            <div key={item.id} style={{ display: "grid", gap: 8, paddingTop: 8, borderTop: "1px solid rgba(148,163,184,0.12)" }}>
              <div style={{ display: "flex", justifyContent: "space-between", gap: 16 }}>
                <strong>v{item.version_number}</strong>
                <StatusBadge value={item.is_final ? "final" : "draft"} />
              </div>
              <div style={{ color: "#c8d6eb" }}>{item.change_summary ?? "Sem resumo"}</div>
              <div style={{ color: "#c8d6eb" }}>Arquivo: {item.storage_key}</div>
            </div>
          ))}
        </div>
      </Card>
    </section>
  );
}
