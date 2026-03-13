# PRD Backend - FBR-Design
> Documento de requisitos tecnicos do backend do sistema FBR-Design.
> Posicionamento: hub criativo central do ecossistema FBR.
> Baseado em workflow, governanca visual, versionamento e integracao entre modulos.

---

## 1. Papel do Sistema no Ecossistema FBR

O `FBR-Design` e a espinha dorsal da operacao criativa da FBR. Seu backend precisa organizar o ciclo completo da demanda visual:

- intake
- classificacao
- triagem
- planejamento
- producao
- revisao
- aprovacao
- versionamento
- entrega
- arquivamento
- reutilizacao

Ele nao e um "gestor de tarefas de arte" e nao deve ser modelado como um gerador visual isolado. O dominio precisa tratar o criativo como ativo operacional com contexto, dono, historico, lineage, regras de uso e relacao com marca, campanha, canal e objetivo de negocio.

O backend deve nascer pronto para dialogar com a maturidade de sistemas como `FBR-Sales`, especialmente em:

- criativos de campanha
- media kits
- branding comercial
- materiais institucionais
- bundles e pacotes comerciais
- entregaveis reutilizaveis
- governanca operacional

---

## 2. Objetivos do Backend

- centralizar demandas vindas de varios sistemas FBR
- transformar briefing em pipeline criativo estruturado
- sustentar status detalhados de producao e SLA
- registrar feedback, aprovacao, retrabalho e excecao sem perda de historico
- versionar ativos e entregaveis com lineage explicito
- preservar biblioteca reutilizavel por marca, projeto, campanha e formato
- viabilizar governanca de identidade visual
- expor contratos seguros para o restante do ecossistema
- criar base para IA assistiva em briefing, classificacao e recuperacao de ativos
- oferecer auditoria operacional e visibilidade executiva

---

## 3. Escopo Funcional

### 3.1 Modulos de dominio

- `Brief Intake`
- `Creative Queue`
- `Production Pipeline`
- `Review & Approval`
- `Asset Library`
- `Templates & Brand Systems`
- `Delivery Center`
- `Creative Analytics`

### 3.2 Capacidades obrigatorias

- entrada manual e integrada de demandas
- enriquecimento de briefing
- classificacao por origem, marca, campanha, canal e criticidade
- decomposicao de entregaveis em `creative_tasks`
- fila por prioridade, urgencia, dependencias e SLA
- workflow de revisao e aprovacao por gates
- versionamento de arquivos e entregaveis
- entrega final com aceite e rastreabilidade
- arquivamento e indexacao para reutilizacao
- sincronizacao segura com outros modulos FBR

---

## 4. Principios de Arquitetura

- sistema interno, single-tenant, orientado ao ecossistema FBR
- nenhum modulo acessa o banco diretamente
- toda integracao acontece por API, eventos ou webhooks autenticados
- storage de arquivo desacoplado do banco
- versionamento, lineage e auditoria sao requisitos centrais
- workflow criativo deve ser configuravel por tipo de demanda e por marca
- IA assistiva apoia classificacao e organizacao, mas nao aprova nem publica sozinha
- ativos precisam carregar contexto de uso e regras de reutilizacao

---

## 5. Stack Recomendada

| Componente | Tecnologia |
|---|---|
| API | FastAPI + Python 3.11+ |
| ORM | SQLAlchemy 2.x |
| Banco | PostgreSQL 16 |
| Cache/eventos leves | Redis 7 |
| Storage | MinIO |
| Migrations | Alembic |
| Auth integracao | JWT interno + API keys + sessao proxy Next.js |
| Observabilidade | Structlog + Prometheus + Grafana |
| Automacoes | n8n |
| Busca textual | PostgreSQL full-text |
| Busca semantica futura | pgvector ou servico dedicado |

### 5.1 Diretriz sobre IA

IA no backend entra como camada assistiva em:

- estruturacao de briefing
- sugestao de classificacao e prioridade
- decomposicao inicial de entregaveis
- indexacao e recuperacao de ativos
- deteccao de lacunas e incoerencias de contexto

A aprovacao humana continua obrigatoria para gates institucionais, mudanca de guideline, liberacao final e substituicao de versao de referencia.

---

## 6. Arquitetura Logica

```text
Sistemas FBR / Frontend Next.js
  -> API Proxy / Webhooks autenticados
  -> FastAPI FBR-Design
      -> Routers
      -> Application Services
      -> Workflow / Policies
      -> Audit / Events
      -> PostgreSQL
      -> Redis
      -> MinIO
      -> Integracoes FBR
      -> Observabilidade
```

### 6.1 Camadas internas

- `Presentation Layer`: routers REST, endpoints internos e webhooks
- `Application Layer`: services, orchestrators, policies e use cases
- `Domain Layer`: entidades, enums, regras de status, aprovacao e SLA
- `Infrastructure Layer`: banco, storage, auth, eventos, auditoria e observabilidade

---

## 7. Modulos e Responsabilidades Tecnicas

### 7.1 Brief Intake

Responsavel por receber, validar e normalizar demandas.

Funcoes:

- receber briefings do painel e de outros sistemas
- validar campos minimos por tipo de demanda
- enriquecer com projeto, marca, campanha, canal e urgencia
- sugerir classificacao inicial por IA
- gerar `design_requests`

### 7.2 Creative Queue

Responsavel pela fila operacional.

Funcoes:

- priorizacao
- estimativa de SLA
- roteamento por especialidade
- agrupamento por campanha, marca, colecao ou sprint
- sinalizacao de bloqueios, aging e urgencias

### 7.3 Production Pipeline

Responsavel por decompor e acompanhar a producao.

Funcoes:

- abrir `creative_tasks`
- registrar dependencias
- mover status detalhados
- anexar arquivos de processo e referencia
- registrar interacoes entre design, redacao, video e solicitante

### 7.4 Review & Approval

Responsavel por governanca e qualidade.

Funcoes:

- threads de feedback
- aprovacao interna
- aprovacao do solicitante
- gates por blueprint
- trilha de rejeicao, retrabalho e nova submissao

### 7.5 Asset Library

Responsavel por memoria e reaproveitamento.

Funcoes:

- registrar ativos finais e intermediarios
- indexar tags, campanhas, marcas, formatos, uso e direitos
- vincular versoes, derivados e reutilizacoes
- permitir colecoes e pacotes reutilizaveis

### 7.6 Templates & Brand Systems

Responsavel por padronizacao visual.

Funcoes:

- templates por projeto, canal, marca e objetivo
- guidelines por marca
- tokens visuais e assets de identidade
- kits visuais para campanhas e operacoes recorrentes

### 7.7 Delivery Center

Responsavel por fechamento operacional.

Funcoes:

- consolidar entregaveis
- disponibilizar download ou distribuicao integrada
- registrar aceite e handoff
- sinalizar destino, uso e recomendacao de reutilizacao

### 7.8 Creative Analytics

Responsavel por inteligencia operacional.

Funcoes:

- medir throughput
- taxa de retrabalho
- lead time por etapa
- gargalos por squad ou marca
- ativos mais reutilizados
- origem de demanda por sistema FBR

---

## 8. Entidades Principais

### 8.1 Core entities

- `projects`
- `brands`
- `campaigns`
- `briefs`
- `request_sources`
- `design_requests`
- `creative_tasks`
- `deliverables`
- `delivery_packages`
- `asset_files`
- `asset_versions`
- `feedback_threads`
- `feedback_entries`
- `approval_steps`
- `templates`
- `template_usages`
- `design_collections`
- `brand_guidelines`
- `brand_tokens`
- `workflow_blueprints`
- `sla_policies`
- `audit_logs`

### 8.2 Entidades de integracao e governanca

- `external_links`
- `integration_events`
- `vendors`
- `cost_entries`
- `request_watchers`
- `request_labels`

---

## 9. Modelo de Dados Conceitual

### 9.1 Relacoes principais

- um `project` possui varias `brands`
- uma `brand` possui varias `brand_guidelines`, `templates` e `design_collections`
- uma `campaign` pode estar ligada a varias `design_requests` e `deliverables`
- um `brief` origina um ou mais `design_requests`
- um `design_request` gera varias `creative_tasks`
- um `design_request` gera um ou mais `deliverables`
- um `deliverable` possui varias `asset_versions`
- um `asset_file` pode compor varios `deliverables`
- um `feedback_thread` pode estar ligado a `design_request`, `creative_task` ou `asset_version`
- um `approval_step` pertence a `deliverable` ou `design_request`
- um `delivery_package` consolida um ou mais `deliverables`

### 9.2 Campos-chave recomendados

#### `briefs`

- `id`
- `source_system`
- `source_reference_id`
- `project_id`
- `brand_id`
- `campaign_id`
- `requester_id`
- `title`
- `objective`
- `audience`
- `channel`
- `constraints`
- `references_summary`
- `ai_intake_notes`
- `created_at`
- `updated_at`

#### `design_requests`

- `id`
- `brief_id`
- `workflow_blueprint_id`
- `project_id`
- `brand_id`
- `campaign_id`
- `source_system`
- `request_type`
- `priority`
- `urgency_level`
- `status`
- `current_stage`
- `round_number`
- `sla_due_at`
- `requested_by`
- `owner_team`
- `assigned_lead_id`
- `risk_level`
- `created_at`
- `updated_at`

#### `creative_tasks`

- `id`
- `design_request_id`
- `task_type`
- `status`
- `assigned_to`
- `depends_on_task_id`
- `started_at`
- `due_at`
- `completed_at`

#### `deliverables`

- `id`
- `design_request_id`
- `deliverable_type`
- `format`
- `status`
- `delivery_channel`
- `final_version_id`
- `approved_at`
- `delivered_at`

#### `asset_versions`

- `id`
- `asset_file_id`
- `version_number`
- `derived_from_version_id`
- `origin_type`
- `storage_key`
- `mime_type`
- `checksum`
- `change_summary`
- `usage_context`
- `approved_by`
- `approved_at`

#### `approval_steps`

- `id`
- `target_type`
- `target_id`
- `step_name`
- `step_order`
- `approver_role`
- `approver_user_id`
- `status`
- `decision`
- `decision_reason`
- `due_at`
- `decided_at`

---

## 10. Fluxos Principais

### 10.1 Fluxo de briefing ate entrega

1. Origem abre um briefing ou envia demanda integrada
2. Sistema normaliza e enriquece a demanda
3. `design_request` e criada com prioridade, SLA e blueprint
4. `creative_tasks` e `deliverables` iniciais sao abertos
5. Time produz, anexa e revisa versoes
6. Gates de revisao e aprovacao sao executados
7. Versao final e marcada explicitamente
8. `Delivery Center` consolida entrega e aceite
9. Ativo entra na biblioteca com lineage e taxonomia

### 10.2 Fluxo de revisao e retrabalho

1. Solicitante ou aprovador pede alteracoes
2. Feedback vira thread estruturada
3. Sistema reabre a etapa correta sem apagar historico
4. Nova versao e gerada
5. Pipeline retorna apenas ao gate necessario

### 10.3 Fluxo de reaproveitamento

1. Entregavel final entra na `Asset Library`
2. Marca, campanha, formato e tags sao indexados
3. Sistema sugere assets e templates relacionados
4. Nova demanda pode derivar de asset existente, preservando lineage

### 10.4 Fluxo de integracao com FBR-Sales

1. `FBR-Sales` abre demanda comercial vinculada a campanha, bundle ou proposta
2. `FBR-Design` gera request com contexto comercial
3. Sistema acompanha criativos, media kits e materiais institucionais
4. Entregaveis aprovados retornam ao contexto comercial como ativos reutilizaveis

---

## 11. Status de Dominio Recomendados

### 11.1 `design_requests.status`

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

### 11.2 `creative_tasks.status`

- `pending`
- `ready`
- `in_progress`
- `blocked`
- `in_review`
- `done`
- `cancelled`

### 11.3 `deliverables.status`

- `not_started`
- `draft_ready`
- `review_ready`
- `approval_pending`
- `approved`
- `delivered`
- `superseded`

### 11.4 `approval_steps.status`

- `pending`
- `open`
- `approved`
- `changes_requested`
- `rejected`
- `skipped`

---

## 12. Regras de Negocio Criticas

- nenhuma aprovacao apaga a versao anterior
- todo retrabalho precisa de motivo estruturado
- toda entrega final precisa apontar origem, responsavel e contexto de uso
- ativos aprovados em um contexto nao ficam liberados para qualquer outro contexto automaticamente
- urgencia muda fila e SLA, nao remove governanca
- uma marca nao usa guideline de outra sem override auditavel
- toda integracao registra `source_system` e `source_reference_id`
- todo deliverable final precisa de `final_version_id`
- reutilizacao relevante deve preservar `derived_from_version_id`

---

## 13. Integracoes com o Ecossistema FBR

### 13.1 `FBR-Sales`

Entradas:

- criativos comerciais
- campanhas por asset e bundle
- media kits
- propostas e materiais institucionais

Saidas:

- status de producao
- entregaveis finais
- ativos comerciais reutilizaveis
- lineage de pecas vinculadas a campanha e bundle

### 13.2 `FBR-MKT`

Entradas:

- campanhas
- branding
- posicionamento
- direcao criativa

Saidas:

- kits visuais
- cronologia de aprovacao
- outputs organizados por campanha

### 13.3 `FBR-Video`

Entradas:

- demandas de thumbnail, KV, lower third e identidade audiovisual

Saidas:

- assets derivados
- guidelines sincronizados
- pacotes visuais reaproveitaveis

### 13.4 `FBR-Redacao`

Entradas:

- copy
- pauta
- contexto editorial

Saidas:

- artes aprovadas
- packs visuais por serie ou campanha

### 13.5 `FBR-Finance`

Entradas:

- centro de custo
- validacao de fornecedor
- regras de aprovacao financeira

Saidas:

- rastreabilidade de custo
- metadados de producao externa

### 13.6 `FBR-Dev`

Entradas:

- storage
- automacoes
- indexacao
- busca
- IA assistiva

Saidas:

- eventos operacionais
- backlog de evolucao tecnica

---

## 14. API e Contratos

### 14.1 Grupos de endpoints

- `/briefs`
- `/design-requests`
- `/creative-tasks`
- `/deliverables`
- `/assets`
- `/asset-versions`
- `/feedback`
- `/approval-steps`
- `/templates`
- `/brand-guidelines`
- `/collections`
- `/analytics`
- `/integrations/*`

### 14.2 Operacoes-chave

- `POST /briefs`
- `POST /design-requests`
- `GET /design-requests`
- `PATCH /design-requests/{id}/priority`
- `PATCH /design-requests/{id}/stage`
- `POST /deliverables/{id}/versions`
- `POST /approval-steps/{id}/approve`
- `POST /approval-steps/{id}/request-changes`
- `POST /feedback/threads`
- `GET /assets/search`
- `GET /analytics/creative-operations`
- `POST /integrations/sales/design-requests`

### 14.3 Padroes de contrato

- responses paginadas por default
- filtros por `project`, `brand`, `campaign`, `channel`, `status`, `priority`, `request_type`
- webhooks assinados
- idempotencia para criacoes vindas de outros sistemas
- campos de integracao padronizados para rastrear origem e sincronizacao

---

## 15. Workflow de Aprovacao

O backend deve suportar workflow configuravel por blueprint.

Exemplos:

- `social_post`: revisao interna -> aprovacao solicitante
- `media_kit`: revisao interna -> aprovacao comercial -> aprovacao solicitante
- `brand_guideline`: revisao design lead -> aprovacao diretoria
- `institutional_deck`: revisao design -> aprovacao marketing -> aprovacao executivo

### 15.1 Requisitos do motor de aprovacao

- etapas sequenciais ou paralelas
- aprovadores por role, time ou usuario
- deadlines por etapa
- motivo estruturado para reprovacao
- reenvio com nova versao sem perda de trilha anterior

---

## 16. Versionamento e Storage

### 16.1 Regras de storage

- binarios vao para MinIO
- metadados, lineage e status ficam no PostgreSQL
- checksum evita duplicidade silenciosa
- URLs assinadas e expiraveis para acesso

### 16.2 Regras de versionamento

- versao numerada por ativo
- `final_version_id` explicito no deliverable
- derivacoes registradas em `derived_from_version_id`
- comparacao por metadados e resumo de mudanca
- toda troca de final precisa gerar log de auditoria

---

## 17. Auditoria e Observabilidade

### 17.1 Auditoria obrigatoria

- criacao e alteracao de briefing
- mudanca de prioridade
- reatribuicao
- aprovacao, rejeicao e pedido de alteracao
- marcacao de versao final
- entrega
- arquivamento
- override de guideline

### 17.2 Telemetria operacional

- volume por origem FBR
- throughput por etapa
- lead time por request type
- taxa de retrabalho
- taxa de aprovacao por rodada
- backlog por marca, campanha e squad
- reutilizacao de ativos por contexto

---

## 18. Requisitos Nao Funcionais

- arquitetura async onde fizer sentido
- soft delete nas entidades aplicaveis
- trilha de auditoria imutavel
- isolamento por roles e ownership
- erros de integracao com retentativa controlada
- uploads com validacao de MIME, extensao, tamanho e magic bytes
- CORS restritivo
- secrets apenas em ambiente seguro
- logs estruturados sem vazamento de dados sensiveis
- latencia previsivel em listagens e filtros criticos

---

## 19. Roles e Permissoes

### 19.1 Perfis base

- `requester`
- `designer`
- `reviewer`
- `creative_lead`
- `sales_manager`
- `marketing_manager`
- `admin`

### 19.2 Regras base

- requester cria, acompanha e comenta
- designer executa tasks e sobe versoes
- reviewer aprova internamente
- creative_lead governa fila, SLA e qualidade
- sales_manager acompanha materiais comerciais e gates associados
- marketing_manager acompanha branding e campanhas
- admin gerencia configuracoes, templates, guidelines e integracoes

---

## 20. Roadmap Tecnico em Camadas

### Fase 1

- briefs
- requests
- fila
- tasks
- versoes
- aprovacao simples
- entrega

### Fase 2

- asset library
- templates e guidelines
- analytics operacional
- integracoes com `FBR-Sales` e `FBR-MKT`

### Fase 3

- workflow blueprint configuravel
- IA assistiva de classificacao
- busca semantica de ativos
- custos, fornecedores e producao externa

### Fase 4

- automacoes ecossistemicas
- recomendacao de reaproveitamento
- score de consistencia de marca
- cockpit executivo criativo

---

## 21. Resumo Executivo

O backend do `FBR-Design` precisa ser concebido como infraestrutura criativa empresarial da FBR. Seu trabalho nao e apenas guardar pecas ou mover cards, mas transformar demanda visual em ativo versionado, aprovado, rastreado, integrado e reutilizavel dentro de um ecossistema cada vez mais maduro.
