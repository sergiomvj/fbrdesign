import { getBriefs } from "@/lib/api";

export default async function IntakePage() {
  const payload = await getBriefs();
  const latestBrief = payload.data[0];

  return (
    <section style={{ display: "grid", gap: 18 }}>
      <div>
        <p style={{ color: "#f97316", textTransform: "uppercase", letterSpacing: "0.18em", fontSize: 12 }}>
          Brief Intake
        </p>
        <h1 style={{ fontSize: 40, marginBottom: 12 }}>Entrada de briefing</h1>
        <p style={{ color: "#c8d6eb", maxWidth: 720 }}>
          Tela inicial preparada para virar wizard. Neste momento, ela ja consome a estrutura de briefing definida no
          contrato do MVP.
        </p>
      </div>

      {latestBrief ? (
        <div style={{ display: "grid", gap: 10, padding: 18, borderRadius: 18, border: "1px solid rgba(148,163,184,0.16)", background: "rgba(20,31,49,0.45)" }}>
          <strong style={{ fontSize: 22 }}>{latestBrief.title}</strong>
          <div>Origem: {latestBrief.source_system}</div>
          <div>Solicitante: {latestBrief.requester_name}</div>
          <div>Objetivo: {latestBrief.objective}</div>
        </div>
      ) : null}
    </section>
  );
}
