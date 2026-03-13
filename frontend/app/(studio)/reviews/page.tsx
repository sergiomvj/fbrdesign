import { getDesignRequests } from "@/lib/api";

import { StatusBadge } from "@/components/studio/StatusBadge";

export default async function ReviewsPage() {
  const payload = await getDesignRequests();
  const pending = payload.data.filter((item) => item.status.includes("approval"));

  return (
    <section style={{ display: "grid", gap: 18 }}>
      <div>
        <p style={{ color: "#f97316", textTransform: "uppercase", letterSpacing: "0.18em", fontSize: 12 }}>
          Review & Approval
        </p>
        <h1 style={{ fontSize: 40, marginBottom: 12 }}>Inbox de aprovacoes</h1>
        <p style={{ color: "#c8d6eb", maxWidth: 720 }}>
          Base inicial da central de revisao. O proximo passo sera acoplar approval steps reais assim que o backend
          expandir esse dominio.
        </p>
      </div>

      <div style={{ display: "grid", gap: 16 }}>
        {pending.map((request) => (
          <div
            key={request.id}
            style={{
              display: "grid",
              gap: 10,
              padding: 18,
              border: "1px solid rgba(148,163,184,0.16)",
              borderRadius: 18,
              background: "rgba(20,31,49,0.45)",
            }}
          >
            <strong style={{ fontSize: 22 }}>{request.request_type}</strong>
            <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
              <StatusBadge value={request.status} />
              <StatusBadge value={request.priority} />
            </div>
            <p style={{ color: "#c8d6eb", margin: 0 }}>Stage atual: {request.current_stage}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
