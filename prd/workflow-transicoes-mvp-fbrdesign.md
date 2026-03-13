# Workflow e Transicoes MVP - FBR-Design
> Matriz operacional inicial de status, transicoes e gates do MVP do `FBR-Design`.
> Objetivo: alinhar banco, API, backend e frontend na mesma logica de operacao.

---

## 1. Objetivo do Workflow

O workflow do `FBR-Design` precisa organizar a operacao criativa sem reduzir o sistema a um quadro de tarefas. O foco do MVP e garantir:

- intake estruturado
- triagem clara
- fila operavel
- producao rastreavel
- revisao interna
- aprovacao por gate
- retrabalho sem perda de historico
- entrega final com versionamento

---

## 2. Objetos com Workflow no MVP

- `design_requests`
- `creative_tasks`
- `deliverables`
- `approval_steps`

---

## 3. Workflow de `design_requests`

### 3.1 Status validos

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

### 3.2 Significado operacional

#### `draft`

Briefing iniciado, ainda nao submetido como demanda formal.

#### `submitted`

Demanda recebida e aguardando triagem.

#### `triaged`

Demanda classificada, com prioridade, contexto e direcao inicial definidos.

#### `queued`

Demanda pronta para entrar em execucao na fila criativa.

#### `in_production`

Tasks e deliverables em producao ativa.

#### `in_internal_review`

Versoes iniciais prontas para avaliacao interna da equipe.

#### `in_stakeholder_approval`

Aprovacao com solicitante, comercial, marketing ou outro gate externo ao design.

#### `changes_requested`

Algum aprovador ou revisor pediu ajustes.

#### `approved`

A demanda foi aprovada no escopo previsto.

#### `delivered`

Output final entregue e registrado.

#### `archived`

Demanda encerrada e mantida como historico.

#### `cancelled`

Demanda interrompida sem continuidade.

### 3.3 Transicoes permitidas

| De | Para | Regra |
|---|---|---|
| `draft` | `submitted` | briefing validado e enviado |
| `submitted` | `triaged` | triagem concluida |
| `triaged` | `queued` | prioridade, SLA e ownership definidos |
| `queued` | `in_production` | primeira task iniciada |
| `in_production` | `in_internal_review` | ao menos um deliverable com versao pronta para revisao |
| `in_internal_review` | `in_stakeholder_approval` | revisao interna aprovada |
| `in_internal_review` | `changes_requested` | revisor interno pediu ajustes |
| `in_stakeholder_approval` | `approved` | todos os gates aprovados |
| `in_stakeholder_approval` | `changes_requested` | gate externo pediu ajustes |
| `changes_requested` | `in_production` | retrabalho retomado |
| `approved` | `delivered` | entrega formal concluida |
| `delivered` | `archived` | encerramento operacional |
| `draft` | `cancelled` | cancelamento antes da submissao |
| `submitted` | `cancelled` | cancelamento antes da execucao |
| `triaged` | `cancelled` | cancelamento antes da producao |
| `queued` | `cancelled` | cancelamento antes da producao |

### 3.4 Transicoes proibidas

- `draft -> approved`
- `submitted -> delivered`
- `queued -> approved`
- `in_production -> delivered`
- `changes_requested -> delivered`
- `approved -> in_production` sem abertura formal de nova rodada

### 3.5 Regras especiais

- ao sair de `changes_requested`, `round_number` deve ser incrementado
- `approved` exige pelo menos um deliverable aprovado
- `delivered` exige `approved_at` e `delivered_at`
- `archived` exige request encerrada e sem gates pendentes

---

## 4. Workflow de `creative_tasks`

### 4.1 Status validos

- `pending`
- `ready`
- `in_progress`
- `blocked`
- `in_review`
- `done`
- `cancelled`

### 4.2 Significado operacional

- `pending`: criada, mas ainda nao liberada
- `ready`: pronta para execucao
- `in_progress`: em trabalho ativo
- `blocked`: travada por dependencia, contexto ou aprovacao
- `in_review`: aguardando validacao interna
- `done`: concluida
- `cancelled`: task encerrada sem execucao completa

### 4.3 Transicoes permitidas

| De | Para |
|---|---|
| `pending` | `ready` |
| `ready` | `in_progress` |
| `in_progress` | `blocked` |
| `blocked` | `in_progress` |
| `in_progress` | `in_review` |
| `in_review` | `done` |
| `in_review` | `in_progress` |
| `pending` | `cancelled` |
| `ready` | `cancelled` |

### 4.4 Regras especiais

- task com dependencia nao pode entrar em `in_progress` antes da predecessora ficar `done`
- task em `done` nao volta para `pending`
- retrabalho deve usar `in_review -> in_progress`, nao recriar historico sem motivo

---

## 5. Workflow de `deliverables`

### 5.1 Status validos

- `not_started`
- `draft_ready`
- `review_ready`
- `approval_pending`
- `approved`
- `delivered`
- `superseded`

### 5.2 Significado operacional

- `not_started`: deliverable criado sem versao util ainda
- `draft_ready`: primeira versao disponivel
- `review_ready`: pronto para revisao interna
- `approval_pending`: aguardando gate externo
- `approved`: aprovado como output valido
- `delivered`: entregue ao destino previsto
- `superseded`: substituido por nova referencia final

### 5.3 Transicoes permitidas

| De | Para |
|---|---|
| `not_started` | `draft_ready` |
| `draft_ready` | `review_ready` |
| `review_ready` | `approval_pending` |
| `review_ready` | `draft_ready` |
| `approval_pending` | `approved` |
| `approval_pending` | `draft_ready` |
| `approved` | `delivered` |
| `approved` | `superseded` |
| `delivered` | `superseded` |

### 5.4 Regras especiais

- `draft_ready` exige ao menos uma `asset_version`
- `approved` exige um `final_version_id`
- `superseded` so ocorre quando outra versao/deliverable substitui a referencia anterior

---

## 6. Workflow de `approval_steps`

### 6.1 Status validos

- `pending`
- `open`
- `approved`
- `changes_requested`
- `rejected`
- `skipped`

### 6.2 Transicoes permitidas

| De | Para |
|---|---|
| `pending` | `open` |
| `open` | `approved` |
| `open` | `changes_requested` |
| `open` | `rejected` |
| `pending` | `skipped` |

### 6.3 Regras especiais

- uma etapa sequencial so pode abrir se a etapa anterior foi `approved` ou `skipped`
- `changes_requested` deve gerar feedback estruturado
- `rejected` encerra o gate atual e exige decisao operacional fora do fluxo padrao do MVP

---

## 7. Gatilhos Entre Objetos

### 7.1 Request -> Tasks

- `triaged -> queued` pode abrir tasks planejadas
- `queued -> in_production` ocorre quando a primeira task entra em `in_progress`

### 7.2 Tasks -> Deliverables

- primeira versao anexada pode mover deliverable para `draft_ready`
- conclusao da task principal de criacao pode mover deliverable para `review_ready`

### 7.3 Deliverables -> Request

- deliverable em `review_ready` pode mover request para `in_internal_review`
- deliverable em `approval_pending` pode mover request para `in_stakeholder_approval`
- deliverable aprovado nao basta sozinho para `request.approved` se ainda houver outro deliverable/gate pendente

### 7.4 Approval -> Request/Deliverable

- gate aprovado pode mover deliverable para `approved`
- gate com `changes_requested` move deliverable para `draft_ready` e request para `changes_requested`

---

## 8. Regras de Rodada e Retrabalho

- toda ida para `changes_requested` abre nova rodada
- `round_number` pertence a `design_requests`
- feedbacks e aprovacoes de rodadas anteriores permanecem preservados
- nova rodada nao apaga `final_version_id` antigo; no maximo marca como superado depois da nova aprovacao

---

## 9. Regras de UI Derivadas do Workflow

- `ConfirmDialog` obrigatorio em aprovacoes e rejeicoes
- badges de status devem usar exatamente os valores oficiais do workflow
- timeline de request deve destacar mudancas de rodada
- deliverables com `approval_pending` devem aparecer no inbox de revisao
- requests em `changes_requested` devem exibir claramente quem pediu ajuste e por que

---

## 10. Regras de API Derivadas do Workflow

- endpoints `PATCH` ou acoes de transicao devem validar transicao permitida
- transicao invalida retorna `409 invalid_transition`
- aprovacoes devem registrar `decision_reason`
- promocao de `final_version_id` deve ser auditada

---

## 11. Casos MVP Prioritarios

### Caso 1 - Post social simples

`draft -> submitted -> triaged -> queued -> in_production -> in_internal_review -> in_stakeholder_approval -> approved -> delivered`

### Caso 2 - Media kit com ajustes comerciais

`draft -> submitted -> triaged -> queued -> in_production -> in_internal_review -> in_stakeholder_approval -> changes_requested -> in_production -> in_internal_review -> in_stakeholder_approval -> approved -> delivered`

### Caso 3 - Demanda cancelada antes da execucao

`draft -> submitted -> triaged -> cancelled`

---

## 12. Resumo Executivo

Esta matriz de workflow cria um idioma operacional unico para o `FBR-Design`. Ela amarra status, transicoes, gates, rounds e retrabalho de forma consistente, permitindo que schema, endpoints, regras de backend e telas do frontend nascam falando exatamente a mesma lingua.
