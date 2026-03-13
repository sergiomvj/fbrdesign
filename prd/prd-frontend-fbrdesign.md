# PRD Frontend - FBR-Design
> Documento de requisitos tecnicos do frontend do sistema FBR-Design.
> Direcao de experiencia: estudio criativo corporativo.
> O produto precisa parecer uma central criativa premium da FBR, nao um dashboard generico.

---

## 1. Papel da Interface

O frontend do `FBR-Design` precisa traduzir visualmente o papel do sistema dentro da FBR: uma central criativa que conecta demanda, criterio, branding, pipeline, aprovacao, entrega e memoria operacional.

A experiencia deve equilibrar tres camadas ao mesmo tempo:

- clareza operacional para fila, SLA, aprovacao e handoff
- densidade criativa para representar pecas, versoes, campanhas, colecoes e guidelines
- presenca institucional para comunicar maturidade e relevancia no ecossistema FBR

O resultado esperado e uma interface com cara de estudio criativo corporativo: sofisticada, precisa, forte, editorial e confiavel.

---

## 2. Objetivos do Frontend

- facilitar abertura de briefing sem cara de formulario burocratico
- tornar a fila criativa priorizavel e legivel
- destacar entregaveis, versoes e feedbacks como objetos centrais
- evidenciar branding, campanha, projeto e reutilizacao
- viabilizar aprovacao com seguranca, rastreabilidade e contexto
- oferecer biblioteca de ativos realmente navegavel
- consolidar analytics operacionais e executivos
- refletir o papel ecossistemico do `FBR-Design`

---

## 3. Direcao Visual

### 3.1 Sensacao de produto

Palavras-guia:

- sofisticado
- criativo
- institucional
- editorial
- contemporaneo
- cirurgico

Evitar:

- visual de SaaS generico
- interface que esconda a dimensao visual do trabalho
- excesso de neutros sem hierarquia
- cara de kanban padrao
- estetica "template tech" sem identidade FBR

### 3.2 Linguagem formal

- titulos fortes e elegantes
- superficies escuras profundas com contraste controlado
- laranja FBR como acento de decisao, nao como cor dominante de tudo
- blocos com profundidade, composicao e respiro
- previews de pecas como parte do layout, nao apenas anexos

### 3.3 Referencia estetica

A pagina conceitual e o produto devem seguir a linha de apresentacao institucional da FBR: dark, refinada, narrativa, premium e visualmente autoral.

---

## 4. Design System

### 4.1 Tipografia

- Titulo e marca: `Outfit`
- Corpo e interface: `Inter`
- Metadados, IDs e status tecnicos: `JetBrains Mono`

### 4.2 Tokens principais

```css
:root {
  --bg: #08111f;
  --bg-2: #0d1728;
  --panel: rgba(20, 31, 49, 0.82);
  --panel-strong: #162235;
  --line: rgba(148, 163, 184, 0.16);
  --text: #eef4ff;
  --muted: #9bb0ca;
  --brand: #f97316;
  --brand-soft: rgba(249, 115, 22, 0.16);
  --success: #22c55e;
  --warning: #f59e0b;
  --danger: #ef4444;
  --info: #38bdf8;
}
```

### 4.3 Componentes com identidade

- cards com profundidade e borda fina
- paineis de preview com tratamento de estudio
- badges de status com leitura imediata
- tabelas com linguagem editorial
- sidebar e topbar com aspecto de sistema premium

---

## 5. Arquitetura de Navegacao

### 5.1 Areas principais

- `Overview`
- `Brief Intake`
- `Creative Queue`
- `Requests`
- `Production`
- `Review & Approval`
- `Asset Library`
- `Templates & Brand Systems`
- `Delivery Center`
- `Creative Analytics`

### 5.2 Estrutura recomendada

```text
app/
  (auth)/
    login/
  (studio)/
    layout.tsx
    page.tsx
    intake/
    requests/
    queue/
    production/
    reviews/
    library/
    templates/
    brands/
    deliveries/
    analytics/
```

### 5.3 Navegacao lateral

Sidebar fixa agrupada por capacidade:

- Studio
- Operacao
- Biblioteca
- Governanca
- Inteligencia

---

## 6. Pilares da Experiencia

### 6.1 Intake sem atrito

O briefing deve ser um wizard orientado por contexto, com progressao clara, carga cognitiva distribuida e ajuda inteligente.

### 6.2 Fila com leitura de decisao

A fila precisa exibir:

- criticidade
- vencimento
- dependencia
- area solicitante
- tipo de entrega
- round de revisao
- risco de SLA

### 6.3 Producao centrada em entregaveis

O objeto central da interface deve ser o entregavel e sua evolucao, nao apenas a task.

### 6.4 Aprovacao sem ambiguidade

O usuario precisa entender:

- o que esta aprovando
- em qual gate esta
- o que acontece se pedir ajustes
- qual versao sera promovida como final

### 6.5 Biblioteca como memoria operacional

A `Asset Library` deve ser navegavel por:

- marca
- projeto
- campanha
- formato
- uso
- tags
- recorrencia

---

## 7. Paginas Principais

### 7.1 `/`

Landing interna do estudio.

Conteudo:

- volume criativo da semana
- backlog em risco
- campanhas ativas
- aprovacoes pendentes
- reutilizacao recente de ativos
- atalhos para novas demandas

### 7.2 `/intake`

Entrada de briefing.

Secoes do wizard:

- contexto e origem
- objetivo da peca ou kit
- conteudo e referencias
- marca, campanha e canal
- anexos e restricoes
- revisao final

IA assistiva:

- sugerir classificacao
- detectar campos faltantes
- propor entregaveis esperados

### 7.3 `/requests`

Visao de demandas abertas.

Recursos:

- tabela editorial com filtros
- agrupamento por marca, campanha, urgencia ou origem
- visao lista e visao board
- SLA e round de revisao visiveis

### 7.4 `/requests/[id]`

Pagina mestra da demanda.

Blocos:

- hero com contexto, prioridade e SLA
- resumo executivo do briefing
- pipeline atual
- tasks vinculadas
- deliverables em producao
- feedback threads
- historico de aprovacoes
- arquivos e versoes

### 7.5 `/queue`

Cockpit de orquestracao criativa.

Recursos:

- filtros por squad, tipo, marca e prazo
- ordenacao por risco
- indicacao de bloqueio e dependencia
- acoes rapidas de reassign, escalate e split

### 7.6 `/production`

Visao de producao em andamento.

Recursos:

- timeline de tarefas
- galerias de versoes
- previews em varios formatos
- comparacao entre versoes

### 7.7 `/reviews`

Central de revisao e aprovacao.

Recursos:

- inbox de aprovacoes pendentes
- comparador de versoes
- feedback contextual
- aprovar, aprovar com ressalvas ou pedir ajustes

### 7.8 `/library`

Biblioteca de ativos.

Recursos:

- busca
- filtros multicamada
- colecoes
- lineage de asset
- derivados e historico de uso

### 7.9 `/templates`

Centro de templates e sistemas visuais.

Recursos:

- templates por projeto, canal, tipo e marca
- preview responsivo
- status de uso
- relacao com brand guidelines

### 7.10 `/brands`

Governanca visual.

Recursos:

- brand profiles
- guidelines
- paletas, tipografia, logos, regras e excecoes
- marcas maes e submarcas

### 7.11 `/deliveries`

Central de entrega.

Recursos:

- pacotes finais
- status de aceite
- links de download
- origem e destino
- reutilizacao recomendada

### 7.12 `/analytics`

Cockpit de performance criativa.

KPIs:

- throughput
- lead time
- tempo por etapa
- taxa de retrabalho
- aprovacao por round
- ativos mais reutilizados
- volume por origem FBR

---

## 8. Componentes-Chave

### 8.1 `StudioShell`

Layout global com sidebar, topbar contextual e area principal fluida.

### 8.2 `RequestHero`

Cabecalho de demanda com:

- titulo
- marca
- campanha
- prioridade
- SLA
- owner
- status

### 8.3 `DeliverableRail`

Trilho ou grid com os entregaveis principais da demanda.

### 8.4 `VersionStack`

Lista visual de versoes com comparacao, metadata e status final.

### 8.5 `ApprovalGate`

Componente de aprovacao com CTA de alto contraste e feedback obrigatorio.

### 8.6 `AssetMosaic`

Grid de biblioteca com previews, tags e indicadores de recorrencia.

### 8.7 `BrandPanel`

Painel visual de guideline, paleta, tipografia e usos recomendados.

### 8.8 `QueueMatrix`

Tabela ou board com risco, aging, dependencia e urgencia.

---

## 9. Estados e Feedback

### 9.1 Loading

- skeletons elegantes com estrutura da pagina real
- placeholders de preview para pecas
- carregamento progressivo de metadados e imagens

### 9.2 Empty states

Devem orientar com tom de estudio:

- sem demanda em risco
- sem ativos nesta colecao
- nenhuma aprovacao pendente

### 9.3 Erros

- mensagens claras
- sem stack trace
- CTA de recuperacao quando possivel

---

## 10. Fluxos de Interface Criticos

### 10.1 Abrir briefing

1. usuario escolhe origem e tipo
2. preenche contexto
3. adiciona referencias e anexos
4. recebe sugestao de classificacao
5. revisa resumo final
6. submete

### 10.2 Revisar e aprovar

1. usuario abre demanda
2. navega por deliverables e versoes
3. comenta pontos especificos
4. aprova ou pede alteracao
5. sistema registra gate e retorno

### 10.3 Reaproveitar asset

1. usuario busca na biblioteca
2. filtra por marca, campanha e formato
3. abre lineage
4. seleciona derivar ou anexar a nova demanda

---

## 11. Integracao Frontend -> Backend

### 11.1 Regra obrigatoria

O frontend nunca chama o backend diretamente no browser. Toda comunicacao passa por rotas `/api/*` no Next.js.

### 11.2 Dominios de API

- `/api/briefs`
- `/api/design-requests`
- `/api/creative-tasks`
- `/api/deliverables`
- `/api/assets`
- `/api/versions`
- `/api/feedback`
- `/api/approvals`
- `/api/templates`
- `/api/brands`
- `/api/analytics`

### 11.3 Hooks principais

- `useStudioOverview`
- `useDesignRequests`
- `useQueue`
- `useDeliverables`
- `useApprovalInbox`
- `useAssetLibrary`
- `useBrandSystems`
- `useCreativeAnalytics`

---

## 12. Requisitos de Seguranca

- sessao via `iron-session` com cookie `httpOnly`
- roles aplicadas em rotas e componentes sensiveis
- nenhuma URL publica permanente para arquivo protegido
- uploads validados no cliente antes do envio
- acoes irreversiveis com `ConfirmDialog`
- mensagens de erro sanitizadas
- nada sensivel em `NEXT_PUBLIC_*`

---

## 13. Requisitos Tecnicos

- Next.js App Router
- TypeScript strict
- Tailwind CSS
- shadcn/ui como base com linguagem personalizada
- componentes de preview e galeria feitos sob medida
- responsivo para desktop e notebook
- mobile com visao reduzida, mantendo estados criticos acessiveis

---

## 14. Fases de Entrega do Frontend

### Fase 1

- shell do estudio
- overview
- intake
- requests
- request detail
- aprovacao basica

### Fase 2

- queue cockpit
- production views
- asset library
- templates
- brands

### Fase 3

- analytics avancado
- comparador de versoes
- recomendacao de reaproveitamento
- assistencia IA no briefing

---

## 15. Resumo Executivo

O frontend do `FBR-Design` precisa fazer o usuario sentir que esta operando o estudio criativo central da FBR. A interface deve mostrar processo e governanca sem matar a natureza visual do trabalho, sustentando tanto a operacao diaria quanto a leitura institucional do sistema.
