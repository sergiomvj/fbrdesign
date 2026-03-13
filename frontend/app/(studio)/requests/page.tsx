import Link from "next/link";

import { StatusBadge } from "@/components/studio/StatusBadge";
import { getDesignRequests } from "@/lib/api";

export default async function RequestsPage() {
  const payload = await getDesignRequests();

  return (
    <section>
      <p style={{ color: "#f97316", textTransform: "uppercase", letterSpacing: "0.18em", fontSize: 12 }}>
        Creative Queue
      </p>
      <h1 style={{ fontSize: 40, marginBottom: 12 }}>Requests</h1>
      <p style={{ color: "#c8d6eb", marginBottom: 24, maxWidth: 720 }}>
        Lista inicial conectada a dados tipados do MVP. Enquanto o backend nao estiver ligado por env, esta tela usa
        fallback mock alinhado aos contratos REST definidos.
      </p>

      <div style={{ display: "grid", gap: 16 }}>
        {payload.data.map((request) => (
          <Link
            key={request.id}
            href={`/requests/${request.id}`}
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
              <strong style={{ fontSize: 22 }}>{request.request_type}</strong>
              <StatusBadge value={request.status} />
            </div>
            <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
              <StatusBadge value={request.priority} />
              <StatusBadge value={request.current_stage} />
            </div>
            <p style={{ color: "#c8d6eb", margin: 0 }}>
              Origem: {request.source_system} • Squad: {request.owner_team ?? "n/d"} • Rodada: {request.round_number}
            </p>
          </Link>
        ))}
      </div>
    </section>
  );
}
