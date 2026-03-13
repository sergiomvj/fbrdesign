# Mapa Inicial de Telas - App Router - FBR-Design
> Estrutura inicial de telas do frontend do `FBR-Design`.
> Objetivo: priorizar implementacao e alinhar as paginas com o dominio do MVP.

---

## 1. Objetivo

Este mapa organiza as telas iniciais do App Router com foco em:

- navegacao clara
- cobertura do fluxo MVP
- alinhamento com requests, deliverables, approvals e library
- ordem de implementacao realista

---

## 2. Estrutura Recomendada

```text
app/
  (auth)/
    login/
      page.tsx
  (studio)/
    layout.tsx
    page.tsx
    intake/
      page.tsx
    requests/
      page.tsx
      [id]/
        page.tsx
    queue/
      page.tsx
    production/
      page.tsx
    reviews/
      page.tsx
    library/
      page.tsx
    templates/
      page.tsx
    brands/
      page.tsx
      [id]/
        page.tsx
    deliveries/
      page.tsx
    analytics/
      page.tsx
```

---

## 3. Prioridade de Implementacao

### P0 - MVP obrigatorio

- `/login`
- `/`
- `/intake`
- `/requests`
- `/requests/[id]`
- `/reviews`

### P1 - Operacao ampliada do MVP

- `/queue`
- `/production`
- `/deliveries`
- `/templates`
- `/brands`

### P2 - Camada de biblioteca e inteligencia

- `/library`
- `/analytics`
- `/brands/[id]`

---

## 4. Descricao por Tela

### 4.1 `/login`

Objetivo:

- autenticar usuario interno

Blocos:

- marca FBR-Design
- formulario de login
- mensagem de erro sanitizada

### 4.2 `/`

Objetivo:

- overview do estudio

Blocos:

- volume criativo da semana
- backlog em risco
- aprovacoes pendentes
- campanhas ativas
- atalhos para `novo briefing`, `requests`, `reviews`

### 4.3 `/intake`

Objetivo:

- abrir nova demanda

Blocos:

- stepper do briefing
- contexto e origem
- objetivo e canal
- referencias e anexos
- marca/campanha
- resumo final

### 4.4 `/requests`

Objetivo:

- listar demandas abertas e encerradas

Blocos:

- filtros
- tabela editorial
- badges de status
- prioridade e SLA
- origem FBR

### 4.5 `/requests/[id]`

Objetivo:

- pagina mestra da demanda

Blocos:

- `RequestHero`
- resumo executivo do briefing
- timeline da request
- tasks vinculadas
- `DeliverableRail`
- `VersionStack`
- feedbacks
- gates de aprovacao

### 4.6 `/reviews`

Objetivo:

- central de aprovacoes

Blocos:

- inbox de gates abertos
- cards por deliverable
- CTA de aprovar/pedir ajustes
- motivos da decisao

### 4.7 `/queue`

Objetivo:

- cockpit de fila criativa

Blocos:

- matriz de risco
- prioridade
- aging
- dependencias
- reassign manual

### 4.8 `/production`

Objetivo:

- visao transversal da producao

Blocos:

- timeline operacional
- versoes recentes
- deliverables em progresso
- tasks bloqueadas

### 4.9 `/deliveries`

Objetivo:

- acompanhar entregas finais

Blocos:

- entregas recentes
- status de aceite
- destino do output
- download e lineage rapido

### 4.10 `/templates`

Objetivo:

- centro de templates

Blocos:

- galeria de templates
- filtros por marca, tipo e canal
- preview
- status de uso

### 4.11 `/brands`

Objetivo:

- listar marcas e sistemas visuais

Blocos:

- cards de marca
- status de guideline
- atalhos para detalhe

### 4.12 `/brands/[id]`

Objetivo:

- detalhe da marca

Blocos:

- painel da marca
- guideline ativa
- templates relacionados
- ativos principais

### 4.13 `/library`

Objetivo:

- biblioteca de ativos

Blocos:

- busca
- filtros multicamada
- mosaic de assets
- lineage

### 4.14 `/analytics`

Objetivo:

- cockpit criativo

Blocos:

- KPIs
- throughput
- retrabalho
- aprovacao por rodada
- origem das demandas

---

## 5. Componentes Compartilhados Essenciais

- `StudioShell`
- `StudioSidebar`
- `StudioTopbar`
- `RequestHero`
- `DeliverableRail`
- `VersionStack`
- `ApprovalGate`
- `QueueMatrix`
- `AssetMosaic`
- `BrandPanel`
- `ConfirmDialog`

---

## 6. Ordem Recomendada da Primeira Sprint de Frontend

1. `layout.tsx` do studio
2. `/login`
3. `/`
4. `/intake`
5. `/requests`
6. `/requests/[id]`
7. `/reviews`

---

## 7. Ordem Recomendada da Segunda Sprint de Frontend

1. `/queue`
2. `/production`
3. `/deliveries`
4. `/templates`
5. `/brands`

---

## 8. Ordem Recomendada da Terceira Sprint de Frontend

1. `/brands/[id]`
2. `/library`
3. `/analytics`

---

## 9. Dependencias Entre Telas

- `/requests/[id]` depende de `GET /design-requests/{id}`
- `/reviews` depende de approvals e deliverables
- `/library` depende de assets/versionamento
- `/brands/[id]` depende de guidelines e templates
- `/analytics` depende de agregacoes backend

---

## 10. Resumo Executivo

Este mapa de telas traduz o dominio do `FBR-Design` em uma navegacao implementavel. A ordem proposta prioriza o caminho critico do MVP, garantindo que o sistema primeiro consiga abrir, operar, revisar e entregar demandas antes de expandir para biblioteca e inteligencia.
