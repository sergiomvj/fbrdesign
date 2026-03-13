"use client";

import { useState, useTransition } from "react";
import type { CSSProperties, FormEvent } from "react";

import { STUDIO_DEFAULTS } from "@/lib/studio-defaults";
import type { BriefCreateResponse, RequestPriority } from "@/types";

const initialState = {
  title: "",
  requester_name: "",
  requester_email: "",
  objective: "",
  request_type: "media_kit",
  priority: "high" as RequestPriority,
  create_linked_request: true,
};

const requestTypes = [
  { value: "media_kit", label: "Media kit" },
  { value: "campaign_kit", label: "Campaign kit" },
  { value: "institutional_piece", label: "Institucional" },
  { value: "social_post", label: "Social post" },
];

const priorities: RequestPriority[] = ["medium", "high", "urgent", "low"];

export function BriefIntakeForm() {
  const [form, setForm] = useState(initialState);
  const [message, setMessage] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  function updateField(field: keyof typeof initialState, value: string | boolean) {
    setForm((current) => ({ ...current, [field]: value }));
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setMessage(null);

    startTransition(async () => {
      const briefResponse = await fetch("/api/briefs", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          source_system: STUDIO_DEFAULTS.sourceSystem,
          project_id: STUDIO_DEFAULTS.projectId,
          brand_id: STUDIO_DEFAULTS.brandId,
          campaign_id: STUDIO_DEFAULTS.campaignId,
          requester_name: form.requester_name,
          requester_email: form.requester_email || null,
          title: form.title,
          objective: form.objective,
          audience: null,
          channel: "internal",
          constraints: null,
          references_summary: null,
          ai_intake_notes: null,
        }),
      });

      if (!briefResponse.ok) {
        setMessage("Nao foi possivel criar o briefing agora.");
        return;
      }

      const briefBody = (await briefResponse.json()) as BriefCreateResponse;
      const briefId = briefBody.data.id;

      if (!form.create_linked_request) {
        setForm(initialState);
        setMessage("Briefing criado com sucesso.");
        return;
      }

      const requestResponse = await fetch("/api/design-requests", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          brief_id: briefId,
          project_id: STUDIO_DEFAULTS.projectId,
          brand_id: STUDIO_DEFAULTS.brandId,
          campaign_id: STUDIO_DEFAULTS.campaignId,
          source_system: STUDIO_DEFAULTS.sourceSystem,
          source_reference_id: null,
          request_type: form.request_type,
          priority: form.priority,
          status: "submitted",
          current_stage: "brief_received",
          owner_team: STUDIO_DEFAULTS.ownerTeam,
          assigned_lead_name: STUDIO_DEFAULTS.assignedLeadName,
          risk_level: STUDIO_DEFAULTS.riskLevel,
          sla_due_at: new Date(Date.now() + 72 * 60 * 60 * 1000).toISOString(),
        }),
      });

      if (!requestResponse.ok) {
        setMessage("Briefing criado, mas a abertura da request criativa falhou.");
        return;
      }

      const requestBody = await requestResponse.json();
      setForm(initialState);
      setMessage(`Briefing e request criativa abertos com sucesso. Request: ${requestBody.data?.id ?? requestBody.id}.`);
    });
  }

  return (
    <form onSubmit={handleSubmit} style={{ display: "grid", gap: 14, maxWidth: 720 }}>
      <input
        value={form.title}
        onChange={(event) => updateField("title", event.target.value)}
        placeholder="Titulo do briefing"
        style={fieldStyle}
        required
      />
      <input
        value={form.requester_name}
        onChange={(event) => updateField("requester_name", event.target.value)}
        placeholder="Solicitante"
        style={fieldStyle}
        required
      />
      <input
        value={form.requester_email}
        onChange={(event) => updateField("requester_email", event.target.value)}
        placeholder="Email do solicitante"
        style={fieldStyle}
        type="email"
      />
      <textarea
        value={form.objective}
        onChange={(event) => updateField("objective", event.target.value)}
        placeholder="Objetivo da demanda"
        style={{ ...fieldStyle, minHeight: 140, resize: "vertical" }}
        required
      />

      <div style={{ display: "grid", gap: 14, gridTemplateColumns: "1fr 1fr" }}>
        <label style={labelStyle}>
          <span>Tipo inicial da request</span>
          <select
            value={form.request_type}
            onChange={(event) => updateField("request_type", event.target.value)}
            style={fieldStyle}
          >
            {requestTypes.map((item) => (
              <option key={item.value} value={item.value}>
                {item.label}
              </option>
            ))}
          </select>
        </label>

        <label style={labelStyle}>
          <span>Prioridade</span>
          <select
            value={form.priority}
            onChange={(event) => updateField("priority", event.target.value as RequestPriority)}
            style={fieldStyle}
          >
            {priorities.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>
        </label>
      </div>

      <label style={{ display: "flex", gap: 10, alignItems: "center", color: "#c8d6eb" }}>
        <input
          checked={form.create_linked_request}
          onChange={(event) => updateField("create_linked_request", event.target.checked)}
          type="checkbox"
        />
        Abrir request criativa automaticamente apos o intake
      </label>

      <button
        type="submit"
        disabled={isPending}
        style={{
          width: "fit-content",
          border: 0,
          borderRadius: 999,
          background: "#f97316",
          color: "#08111f",
          fontWeight: 700,
          padding: "12px 18px",
          cursor: "pointer",
        }}
      >
        {isPending ? "Enviando..." : "Criar briefing"}
      </button>
      {message ? <p style={{ color: "#c8d6eb", margin: 0 }}>{message}</p> : null}
    </form>
  );
}

const labelStyle: CSSProperties = {
  display: "grid",
  gap: 8,
  color: "#c8d6eb",
};

const fieldStyle: CSSProperties = {
  width: "100%",
  borderRadius: 14,
  border: "1px solid rgba(148,163,184,0.16)",
  background: "rgba(20,31,49,0.45)",
  color: "#eef4ff",
  padding: "14px 16px",
};
