# Backlog Tecnico MVP - FBR-Design
> Backlog executavel inicial do MVP do `FBR-Design`.
> Organizado por frentes de trabalho para facilitar planejamento de sprint e implementacao.

---

## 1. Prioridades Gerais

### Prioridade P0

- schema relacional
- migrations iniciais
- dominio de requests e deliverables
- versionamento de ativos
- approvals e feedback
- shell frontend
- intake
- request detail

### Prioridade P1

- templates
- brands/guidelines
- queue
- analytics inicial
- integracao MVP com `FBR-Sales`

### Prioridade P2

- `FBR-MKT`
- `FBR-Video`
- `FBR-Redacao`
- observabilidade avancada
- automacoes assistivas

---

## 2. Backend

### 2.1 Fundacao

- [ ] Criar estrutura inicial do app FastAPI
- [ ] Configurar `settings` e secrets
- [ ] Configurar SQLAlchemy 2.x
- [ ] Configurar Alembic
- [ ] Configurar cliente MinIO
- [ ] Configurar logs estruturados

### 2.2 Banco e dominio

- [ ] Implementar migration de `projects`
- [ ] Implementar migration de `brands`
- [ ] Implementar migration de `campaigns`
- [ ] Implementar migration de `briefs`
- [ ] Implementar migration de `design_requests`
- [ ] Implementar migration de `creative_tasks`
- [ ] Implementar migration de `deliverables`
- [ ] Implementar migration de `asset_files`
- [ ] Implementar migration de `asset_versions`
- [ ] Implementar migration de `feedback_threads`
- [ ] Implementar migration de `feedback_entries`
- [ ] Implementar migration de `approval_steps`
- [ ] Implementar migration de `templates`
- [ ] Implementar migration de `brand_guidelines`
- [ ] Implementar migration de `audit_logs`

### 2.3 Services

- [ ] Criar `brief_service`
- [ ] Criar `design_request_service`
- [ ] Criar `creative_task_service`
- [ ] Criar `deliverable_service`
- [ ] Criar `asset_version_service`
- [ ] Criar `feedback_service`
- [ ] Criar `approval_service`
- [ ] Criar `template_service`
- [ ] Criar `brand_service`
- [ ] Criar `audit_service`

### 2.4 Routers

- [ ] Implementar `POST /briefs`
- [ ] Implementar `GET /briefs/{id}`
- [ ] Implementar `POST /design-requests`
- [ ] Implementar `GET /design-requests`
- [ ] Implementar `GET /design-requests/{id}`
- [ ] Implementar `PATCH /design-requests/{id}`
- [ ] Implementar `POST /design-requests/{id}/tasks`
- [ ] Implementar `PATCH /creative-tasks/{id}`
- [ ] Implementar `POST /design-requests/{id}/deliverables`
- [ ] Implementar `GET /deliverables/{id}`
- [ ] Implementar `PATCH /deliverables/{id}`
- [ ] Implementar `POST /deliverables/{id}/versions`
- [ ] Implementar `POST /feedback/threads`
- [ ] Implementar `POST /feedback/threads/{id}/entries`
- [ ] Implementar `POST /approval-steps`
- [ ] Implementar `POST /approval-steps/{id}/approve`
- [ ] Implementar `POST /approval-steps/{id}/request-changes`
- [ ] Implementar `GET /templates`
- [ ] Implementar `POST /templates`
- [ ] Implementar `GET /brands`
- [ ] Implementar `GET /brands/{id}`

### 2.5 Regras de workflow

- [ ] Definir matriz de transicoes de `design_requests`
- [ ] Definir matriz de transicoes de `creative_tasks`
- [ ] Definir matriz de transicoes de `deliverables`
- [ ] Definir regras de round/retrabalho
- [ ] Definir promocao de `final_version_id`
- [ ] Definir criacao automatica de gates por tipo de request

---

## 3. Frontend

### 3.1 Fundacao

- [ ] Criar app Next.js com App Router
- [ ] Configurar Tailwind
- [ ] Configurar tokens visuais
- [ ] Configurar fontes `Outfit`, `Inter` e `JetBrains Mono`
- [ ] Criar shell `StudioShell`
- [ ] Criar navegacao lateral por dominios

### 3.2 Intake e requests

- [ ] Implementar pagina `/`
- [ ] Implementar pagina `/intake`
- [ ] Criar wizard de briefing
- [ ] Criar resumo final de submissao
- [ ] Implementar pagina `/requests`
- [ ] Implementar pagina `/requests/[id]`
- [ ] Criar `RequestHero`
- [ ] Criar `DeliverableRail`
- [ ] Criar `VersionStack`
- [ ] Criar `ApprovalGate`

### 3.3 Biblioteca e governanca

- [ ] Implementar pagina `/library`
- [ ] Implementar `AssetMosaic`
- [ ] Implementar pagina `/templates`
- [ ] Implementar pagina `/brands`
- [ ] Criar `BrandPanel`

### 3.4 Operacao

- [ ] Implementar pagina `/queue`
- [ ] Criar `QueueMatrix`
- [ ] Implementar pagina `/production`
- [ ] Implementar pagina `/reviews`
- [ ] Implementar pagina `/deliveries`
- [ ] Implementar pagina `/analytics`

---

## 4. Integracoes

### 4.1 FBR-Sales

- [ ] Definir payload de origem de demanda comercial
- [ ] Definir campo para bundle/proposal/campaign no contexto da request
- [ ] Criar endpoint de entrada integrado
- [ ] Criar retorno de status de producao
- [ ] Criar retorno de entregaveis finais reutilizaveis

### 4.2 FBR-MKT

- [ ] Definir payload de campanhas e branding
- [ ] Criar contrato de entrada para demandas estrategicas
- [ ] Criar retorno de kits visuais e status

### 4.3 Outros modulos

- [ ] Mapear dependencias com `FBR-Video`
- [ ] Mapear dependencias com `FBR-Redacao`
- [ ] Mapear metadados financeiros para `FBR-Finance`
- [ ] Definir eventos tecnicos com `FBR-Dev`

---

## 5. Observabilidade e Seguranca

### 5.1 Observabilidade

- [ ] Adicionar healthcheck basico
- [ ] Adicionar logs estruturados
- [ ] Adicionar metricas Prometheus
- [ ] Criar dashboard Grafana inicial

### 5.2 Seguranca

- [ ] Definir estrategia de autenticacao interna
- [ ] Definir autorizacao por role
- [ ] Validar uploads por tipo, tamanho e magic bytes
- [ ] Sanitizar mensagens de erro
- [ ] Implementar CORS restritivo
- [ ] Garantir trilha de auditoria nas acoes irreversiveis

---

## 6. Ordem Recomendada da Primeira Sprint de Implementacao

1. FastAPI base + settings + DB
2. Alembic + migrations centrais
3. `briefs` e `design_requests`
4. `deliverables` e `asset_versions`
5. `feedback_threads` e `approval_steps`
6. Next.js shell + intake
7. requests list + request detail
8. integracao MVP com `FBR-Sales`

---

## 7. Criterio de Saida do MVP Tecnico

O MVP tecnico pode ser considerado funcional quando:

- um briefing vira `design_request`
- a request gera deliverable
- o deliverable recebe versoes
- o sistema registra feedback
- o sistema executa gate de aprovacao
- o frontend consegue abrir, acompanhar e revisar a demanda
- ha pelo menos um fluxo integrado com `FBR-Sales`

---

## 8. Resumo Executivo

Este backlog transforma a visao do `FBR-Design` em uma fila clara de implementacao. Ele separa o trabalho por frente tecnica, preserva prioridade de negocio e reduz o risco de o projeto virar apenas mais um painel bonito sem dominio real por tras.
