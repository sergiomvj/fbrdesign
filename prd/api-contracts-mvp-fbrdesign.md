# API Contracts MVP - FBR-Design
> Contratos REST iniciais do MVP do `FBR-Design`.
> Objetivo: definir os endpoints centrais para implementacao backend/frontend.

---

## 1. Principios de Contrato

- JSON em todas as requests/responses
- autenticacao via sessao proxy no frontend e headers internos no backend
- paginacao por default em listagens
- filtros por query string
- timestamps em ISO 8601
- respostas de erro sanitizadas

Formato base recomendado:

```json
{
  "data": {},
  "meta": {},
  "error": null
}
```

---

## 2. Entidades Prioritarias do MVP

- `briefs`
- `design_requests`
- `creative_tasks`
- `deliverables`
- `asset_versions`
- `feedback_threads`
- `approval_steps`
- `templates`
- `brands`

---

## 3. Briefs

### `POST /briefs`

Cria um briefing.

Request:

```json
{
  "source_system": "fbr_sales",
  "source_reference_id": "sales-campaign-128",
  "project_id": "uuid",
  "brand_id": "uuid",
  "campaign_id": "uuid",
  "requester_name": "Ana Lima",
  "requester_email": "ana@fbr.com",
  "title": "Media kit institucional 2026",
  "objective": "Atualizar material comercial da unidade",
  "audience": "Parceiros e anunciantes",
  "channel": "commercial",
  "constraints": "Usar linguagem institucional",
  "references_summary": "Basear no kit do ano passado"
}
```

Response:

```json
{
  "data": {
    "id": "uuid",
    "status": "created"
  },
  "meta": {},
  "error": null
}
```

### `GET /briefs/{id}`

Retorna um briefing.

---

## 4. Design Requests

### `POST /design-requests`

Cria uma request a partir de briefing.

Request:

```json
{
  "brief_id": "uuid",
  "request_type": "media_kit",
  "priority": "high",
  "current_stage": "triage",
  "owner_team": "design",
  "sla_due_at": "2026-03-15T18:00:00Z"
}
```

Response:

```json
{
  "data": {
    "id": "uuid",
    "status": "submitted",
    "round_number": 1
  },
  "meta": {},
  "error": null
}
```

### `GET /design-requests`

Lista requests com filtros.

Query params suportados:

- `status`
- `priority`
- `project_id`
- `brand_id`
- `campaign_id`
- `request_type`
- `page`
- `page_size`

### `GET /design-requests/{id}`

Retorna a pagina de detalhe agregada da request.

Response agregada recomendada:

```json
{
  "data": {
    "request": {},
    "brief": {},
    "tasks": [],
    "deliverables": [],
    "approval_steps": [],
    "feedback_threads": []
  },
  "meta": {},
  "error": null
}
```

### `PATCH /design-requests/{id}`

Atualiza campos controlados.

Campos permitidos no MVP:

- `priority`
- `status`
- `current_stage`
- `owner_team`
- `risk_level`
- `sla_due_at`

---

## 5. Creative Tasks

### `POST /design-requests/{id}/tasks`

Cria uma task vinculada a uma request.

Request:

```json
{
  "task_type": "layout",
  "title": "Montar primeira versao do media kit",
  "description": "Usar guideline institucional da marca",
  "assigned_to_name": "Equipe Design",
  "due_at": "2026-03-14T18:00:00Z"
}
```

### `PATCH /creative-tasks/{id}`

Atualiza status ou atribuicao.

Campos permitidos:

- `status`
- `assigned_to_name`
- `due_at`

---

## 6. Deliverables

### `POST /design-requests/{id}/deliverables`

Cria um deliverable.

Request:

```json
{
  "deliverable_type": "media_kit",
  "name": "Media Kit 2026",
  "format": "pdf",
  "channel": "commercial",
  "delivery_channel": "fbr_sales"
}
```

### `GET /deliverables/{id}`

Retorna deliverable com versoes e aprovacoes.

### `PATCH /deliverables/{id}`

Campos permitidos:

- `status`
- `delivery_channel`
- `final_version_id`

### `POST /deliverables/{id}/versions`

Registra nova versao de arquivo.

Request:

```json
{
  "asset_file_name": "media-kit-2026.pdf",
  "storage_bucket": "fbr-design-assets",
  "storage_key": "brands/facebrasil/media-kit-v2.pdf",
  "mime_type": "application/pdf",
  "file_size_bytes": 1820332,
  "checksum": "sha256-hash",
  "origin_type": "designer_upload",
  "change_summary": "Ajuste de capa e pagina comercial"
}
```

Response:

```json
{
  "data": {
    "asset_file_id": "uuid",
    "version_id": "uuid",
    "version_number": 2
  },
  "meta": {},
  "error": null
}
```

---

## 7. Feedback

### `POST /feedback/threads`

Cria uma thread.

Request:

```json
{
  "target_type": "deliverable",
  "target_id": "uuid",
  "design_request_id": "uuid",
  "title": "Ajustes solicitados no bloco comercial",
  "created_by_name": "Comercial"
}
```

### `POST /feedback/threads/{id}/entries`

Adiciona comentario.

Request:

```json
{
  "author_name": "Mariana Sales",
  "author_role": "sales_manager",
  "message": "Precisamos reforcar os beneficios do bundle premium.",
  "is_change_request": true
}
```

---

## 8. Approval Steps

### `POST /approval-steps`

Cria gate de aprovacao.

Request:

```json
{
  "target_type": "deliverable",
  "target_id": "uuid",
  "design_request_id": "uuid",
  "deliverable_id": "uuid",
  "step_order": 1,
  "step_name": "Aprovacao comercial",
  "approver_role": "sales_manager",
  "due_at": "2026-03-15T15:00:00Z"
}
```

### `POST /approval-steps/{id}/approve`

Request:

```json
{
  "approver_name": "Carlos Sales",
  "decision_reason": "Aprovado para uso comercial"
}
```

### `POST /approval-steps/{id}/request-changes`

Request:

```json
{
  "approver_name": "Carlos Sales",
  "decision_reason": "Atualizar pagina de bundles e CTA final"
}
```

---

## 9. Templates

### `GET /templates`

Lista templates com filtros:

- `brand_id`
- `project_id`
- `template_type`
- `channel`
- `status`

### `POST /templates`

Cria template.

### `PATCH /templates/{id}`

Atualiza template.

### `DELETE /templates/{id}`

Soft delete.

---

## 10. Brands

### `GET /brands`

Lista marcas.

### `GET /brands/{id}`

Retorna marca com guidelines resumidas.

### `POST /brands`

Cria marca.

### `PATCH /brands/{id}`

Atualiza marca.

---

## 11. Responses de Erro

Formato recomendado:

```json
{
  "data": null,
  "meta": {},
  "error": {
    "code": "validation_error",
    "message": "Dados invalidos para criar o briefing."
  }
}
```

Codigos iniciais:

- `validation_error`
- `not_found`
- `forbidden`
- `conflict`
- `invalid_transition`
- `storage_error`

---

## 12. Ordem Recomendada de Implementacao

1. `POST /briefs`
2. `POST /design-requests`
3. `GET /design-requests`
4. `GET /design-requests/{id}`
5. `POST /design-requests/{id}/tasks`
6. `POST /design-requests/{id}/deliverables`
7. `POST /deliverables/{id}/versions`
8. `POST /feedback/threads`
9. `POST /feedback/threads/{id}/entries`
10. `POST /approval-steps`
11. `POST /approval-steps/{id}/approve`
12. `POST /approval-steps/{id}/request-changes`
13. `GET /templates`
14. `GET /brands`

---

## 13. Resumo Executivo

Estes contratos REST cobrem o nucleo do MVP do `FBR-Design`: abrir demanda, operar pipeline, registrar versoes, coletar feedback, executar aprovacoes e governar ativos reutilizaveis. Eles servem como ponte direta entre os PRDs conceituais e a implementacao backend/frontend.
