# Schema Relacional Inicial - FBR-Design
> Base relacional inicial do MVP do `FBR-Design`.
> Objetivo: traduzir o dominio conceitual em estrutura implementavel para PostgreSQL.

---

## 1. Objetivo do Schema

Este schema inicial cobre o nucleo operacional do `FBR-Design`:

- briefing
- requests
- tasks
- deliverables
- versionamento
- feedback
- aprovacao
- templates
- brands
- auditoria

Ele foi desenhado para atender o MVP sem bloquear a expansao futura para:

- colecoes
- custos e fornecedores
- workflow blueprints avancados
- busca semantica
- reutilizacao inteligente

---

## 2. Convencoes Gerais

- banco alvo: PostgreSQL 16
- chaves primarias em `uuid`
- campos de data em `timestamptz`
- tabelas operacionais com `created_at` e `updated_at`
- soft delete em tabelas aplicaveis com `deleted_at`
- auditoria imutavel em tabela separada
- enums podem nascer em PostgreSQL ou na camada SQLAlchemy, mas devem manter os mesmos valores

---

## 3. Enums Iniciais

### 3.1 `source_system_enum`

- `fbr_sales`
- `fbr_mkt`
- `fbr_video`
- `fbr_redacao`
- `fbr_click`
- `fbr_leads`
- `fbr_finance`
- `fbr_dev`
- `internal_manual`

### 3.2 `request_priority_enum`

- `low`
- `medium`
- `high`
- `urgent`

### 3.3 `design_request_status_enum`

- `draft`
- `submitted`
- `triaged`
- `queued`
- `in_production`
- `in_internal_review`
- `in_stakeholder_approval`
- `changes_requested`
- `approved`
- `delivered`
- `archived`
- `cancelled`

### 3.4 `creative_task_status_enum`

- `pending`
- `ready`
- `in_progress`
- `blocked`
- `in_review`
- `done`
- `cancelled`

### 3.5 `deliverable_status_enum`

- `not_started`
- `draft_ready`
- `review_ready`
- `approval_pending`
- `approved`
- `delivered`
- `superseded`

### 3.6 `approval_status_enum`

- `pending`
- `open`
- `approved`
- `changes_requested`
- `rejected`
- `skipped`

### 3.7 `feedback_target_enum`

- `design_request`
- `creative_task`
- `deliverable`
- `asset_version`

### 3.8 `deliverable_type_enum`

- `social_post`
- `banner`
- `presentation`
- `media_kit`
- `brand_asset`
- `institutional_piece`
- `thumbnail`
- `campaign_kit`
- `editorial_piece`

---

## 4. Tabelas Principais

### 4.1 `projects`

Representa um projeto ou iniciativa do ecossistema FBR.

Campos:

- `id uuid pk`
- `code varchar(50) unique not null`
- `name varchar(150) not null`
- `description text null`
- `is_active boolean not null default true`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`

### 4.2 `brands`

Marcas maes, submarcas ou identidades atreladas a um projeto.

Campos:

- `id uuid pk`
- `project_id uuid fk -> projects.id`
- `parent_brand_id uuid fk -> brands.id null`
- `name varchar(150) not null`
- `slug varchar(150) unique not null`
- `status varchar(30) not null default 'active'`
- `primary_color varchar(20) null`
- `secondary_color varchar(20) null`
- `notes text null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

### 4.3 `campaigns`

Campanhas ou frentes criativas ligadas a requests e entregaveis.

Campos:

- `id uuid pk`
- `project_id uuid fk -> projects.id`
- `brand_id uuid fk -> brands.id`
- `source_system source_system_enum not null`
- `source_reference_id varchar(120) null`
- `name varchar(180) not null`
- `objective text null`
- `starts_at timestamptz null`
- `ends_at timestamptz null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

### 4.4 `briefs`

Documento de entrada estruturado da demanda.

Campos:

- `id uuid pk`
- `source_system source_system_enum not null`
- `source_reference_id varchar(120) null`
- `project_id uuid fk -> projects.id`
- `brand_id uuid fk -> brands.id`
- `campaign_id uuid fk -> campaigns.id null`
- `requester_name varchar(150) not null`
- `requester_email varchar(180) null`
- `title varchar(180) not null`
- `objective text not null`
- `audience text null`
- `channel varchar(120) null`
- `constraints text null`
- `references_summary text null`
- `ai_intake_notes text null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

### 4.5 `design_requests`

Entidade central da operacao criativa.

Campos:

- `id uuid pk`
- `brief_id uuid fk -> briefs.id`
- `project_id uuid fk -> projects.id`
- `brand_id uuid fk -> brands.id`
- `campaign_id uuid fk -> campaigns.id null`
- `source_system source_system_enum not null`
- `source_reference_id varchar(120) null`
- `request_type varchar(80) not null`
- `priority request_priority_enum not null`
- `status design_request_status_enum not null`
- `current_stage varchar(80) not null`
- `round_number integer not null default 1`
- `owner_team varchar(80) null`
- `assigned_lead_name varchar(150) null`
- `risk_level varchar(30) null`
- `sla_due_at timestamptz null`
- `requested_at timestamptz not null`
- `approved_at timestamptz null`
- `delivered_at timestamptz null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

### 4.6 `creative_tasks`

Unidades operacionais internas da demanda.

Campos:

- `id uuid pk`
- `design_request_id uuid fk -> design_requests.id`
- `parent_task_id uuid fk -> creative_tasks.id null`
- `task_type varchar(80) not null`
- `title varchar(180) not null`
- `description text null`
- `status creative_task_status_enum not null`
- `assigned_to_name varchar(150) null`
- `depends_on_task_id uuid fk -> creative_tasks.id null`
- `started_at timestamptz null`
- `due_at timestamptz null`
- `completed_at timestamptz null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

### 4.7 `deliverables`

Saidas criativas vinculadas a uma request.

Campos:

- `id uuid pk`
- `design_request_id uuid fk -> design_requests.id`
- `deliverable_type deliverable_type_enum not null`
- `name varchar(180) not null`
- `format varchar(60) not null`
- `channel varchar(120) null`
- `status deliverable_status_enum not null`
- `delivery_channel varchar(120) null`
- `final_version_id uuid null`
- `approved_at timestamptz null`
- `delivered_at timestamptz null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

Observacao:

- `final_version_id` deve ser FK para `asset_versions.id`, adicionada apos a criacao da tabela `asset_versions`

### 4.8 `asset_files`

Representa o ativo logico pai do versionamento.

Campos:

- `id uuid pk`
- `design_request_id uuid fk -> design_requests.id null`
- `deliverable_id uuid fk -> deliverables.id null`
- `brand_id uuid fk -> brands.id null`
- `campaign_id uuid fk -> campaigns.id null`
- `name varchar(180) not null`
- `file_kind varchar(60) not null`
- `mime_group varchar(40) null`
- `tags text null`
- `usage_context text null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

### 4.9 `asset_versions`

Versoes fisicas de um ativo.

Campos:

- `id uuid pk`
- `asset_file_id uuid fk -> asset_files.id`
- `version_number integer not null`
- `derived_from_version_id uuid fk -> asset_versions.id null`
- `storage_key varchar(255) not null`
- `storage_bucket varchar(120) not null`
- `mime_type varchar(120) not null`
- `file_size_bytes bigint not null`
- `checksum varchar(128) not null`
- `origin_type varchar(60) not null`
- `change_summary text null`
- `is_final boolean not null default false`
- `approved_by_name varchar(150) null`
- `approved_at timestamptz null`
- `created_at timestamptz not null`

Restricoes recomendadas:

- unique (`asset_file_id`, `version_number`)
- unique (`checksum`) opcional se a estrategia de deduplicacao for global

### 4.10 `feedback_threads`

Agrupador de feedback por alvo.

Campos:

- `id uuid pk`
- `target_type feedback_target_enum not null`
- `target_id uuid not null`
- `design_request_id uuid fk -> design_requests.id`
- `status varchar(30) not null default 'open'`
- `title varchar(180) null`
- `created_by_name varchar(150) not null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`

### 4.11 `feedback_entries`

Entradas de comentario e retorno.

Campos:

- `id uuid pk`
- `thread_id uuid fk -> feedback_threads.id`
- `author_name varchar(150) not null`
- `author_role varchar(80) null`
- `message text not null`
- `is_change_request boolean not null default false`
- `created_at timestamptz not null`

### 4.12 `approval_steps`

Gates de aprovacao configurados por deliverable ou request.

Campos:

- `id uuid pk`
- `target_type varchar(40) not null`
- `target_id uuid not null`
- `design_request_id uuid fk -> design_requests.id`
- `deliverable_id uuid fk -> deliverables.id null`
- `step_order integer not null`
- `step_name varchar(120) not null`
- `approver_role varchar(80) null`
- `approver_name varchar(150) null`
- `status approval_status_enum not null`
- `decision_reason text null`
- `due_at timestamptz null`
- `decided_at timestamptz null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`

### 4.13 `templates`

Templates reutilizaveis por marca/projeto/canal.

Campos:

- `id uuid pk`
- `project_id uuid fk -> projects.id null`
- `brand_id uuid fk -> brands.id null`
- `name varchar(180) not null`
- `slug varchar(180) unique not null`
- `template_type varchar(80) not null`
- `channel varchar(120) null`
- `description text null`
- `preview_asset_file_id uuid fk -> asset_files.id null`
- `status varchar(30) not null default 'active'`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

### 4.14 `brand_guidelines`

Regras e sistemas visuais de marca.

Campos:

- `id uuid pk`
- `brand_id uuid fk -> brands.id`
- `version_label varchar(60) not null`
- `status varchar(30) not null default 'draft'`
- `summary text null`
- `rules_text text null`
- `cover_asset_file_id uuid fk -> asset_files.id null`
- `published_at timestamptz null`
- `created_at timestamptz not null`
- `updated_at timestamptz not null`
- `deleted_at timestamptz null`

### 4.15 `audit_logs`

Trilha imutavel de eventos relevantes.

Campos:

- `id uuid pk`
- `entity_type varchar(80) not null`
- `entity_id uuid not null`
- `action varchar(80) not null`
- `actor_name varchar(150) null`
- `actor_role varchar(80) null`
- `metadata_json jsonb not null default '{}'::jsonb`
- `created_at timestamptz not null`

---

## 5. Relacoes Criticas

- `briefs 1:n design_requests`
- `design_requests 1:n creative_tasks`
- `design_requests 1:n deliverables`
- `deliverables 1:n asset_files`
- `asset_files 1:n asset_versions`
- `design_requests 1:n feedback_threads`
- `feedback_threads 1:n feedback_entries`
- `design_requests 1:n approval_steps`
- `deliverables 1:n approval_steps`
- `brands 1:n templates`
- `brands 1:n brand_guidelines`

---

## 6. Indices Recomendados

### 6.1 Operacionais

- `design_requests (status, priority, sla_due_at)`
- `design_requests (project_id, brand_id, campaign_id)`
- `creative_tasks (design_request_id, status, due_at)`
- `deliverables (design_request_id, status)`
- `approval_steps (status, due_at)`
- `audit_logs (entity_type, entity_id, created_at desc)`

### 6.2 Busca e biblioteca

- `templates (brand_id, template_type, status)`
- `asset_files (brand_id, campaign_id)`
- `asset_versions (asset_file_id, version_number desc)`
- GIN em campos textuais indexados de template/brief se houver full-text

---

## 7. Regras de Integridade Importantes

- `design_requests.round_number >= 1`
- `creative_tasks` nao podem depender de task de outra request
- `asset_versions.version_number` deve ser sequencial por `asset_file_id`
- `deliverables.final_version_id` deve apontar para uma versao pertencente ao deliverable
- `approval_steps.step_order` deve ser unico por alvo
- `audit_logs` nao usa soft delete nem update de conteudo

---

## 8. Ordem Recomendada de Implementacao

1. `projects`
2. `brands`
3. `campaigns`
4. `briefs`
5. `design_requests`
6. `creative_tasks`
7. `deliverables`
8. `asset_files`
9. `asset_versions`
10. `feedback_threads`
11. `feedback_entries`
12. `approval_steps`
13. `templates`
14. `brand_guidelines`
15. `audit_logs`
16. adicionar FK de `deliverables.final_version_id -> asset_versions.id`

---

## 9. Escopo de Fora deste Schema Inicial

- fornecedores e custo detalhado
- collections e delivery packages completos
- watchers e labels
- workflow blueprints persistidos
- score de consistencia de marca
- embeddings e busca semantica persistida

---

## 10. Resumo Executivo

Este schema inicial cria uma base relacional suficiente para o MVP do `FBR-Design` operar briefing, pipeline, versoes, aprovacao, templates e governanca visual. Ele foi propositalmente desenhado para nascer simples o bastante para implementar agora, mas sem comprometer a expansao futura do sistema como hub criativo central do ecossistema FBR.
