# Implementation Plan - FBR-Design
> Plano de implementacao do sistema FBR-Design.
> Direcao: hub criativo central do ecossistema FBR.
> Objetivo: sair do conceito e chegar a um produto implementavel, integrado e governavel.

---

## 1. Norte do Produto

**Sistema:** FBR-Design  
**Papel:** central criativa, visual e de branding da FBR  
**Posicionamento:** estudio criativo corporativo com operacao estruturada  
**Tipo de plataforma:** sistema interno, single-tenant, integrado ao ecossistema FBR

O `FBR-Design` nao deve ser implantado como "ferramenta de geracao de artes" nem como "kanban de pecas". O plano abaixo assume que o sistema precisa nascer preparado para:

- intake de demandas multiorigem
- pipeline criativo detalhado
- revisao e aprovacao em gates
- versionamento e lineage de ativos
- biblioteca reutilizavel
- governanca de marca
- analytics operacional e executivo
- integracao futura com a maturidade do `FBR-Sales`

---

## 2. Principios de Implementacao

- priorizar arquitetura de dominio antes de automacoes sofisticadas
- separar claramente requests, tasks, deliverables e assets
- tratar arquivo como ativo com historico, nao como anexo solto
- garantir auditabilidade desde o MVP
- integrar com outros sistemas via API/eventos, nunca por acoplamento de banco
- deixar IA como camada assistiva, nunca como decisor final
- preservar coerencia com a familia FBR e espaco para crescimento de maturidade

---

## 3. Macro Fases

| Fase | Objetivo | Saida principal |
|---|---|---|
| 01 | Fundacao de dominio | modelo, fluxos, entidades e contratos coerentes |
| 02 | Backend core | API, banco, workflow, versionamento e integracoes base |
| 03 | Frontend studio | shell, intake, queue, requests, approvals e library |
| 04 | Integracoes FBR | contratos com Sales, MKT, Video, Redacao, Finance e Dev |
| 05 | IA assistiva e analytics | apoio ao briefing, organizacao e cockpit criativo |
| 06 | Hardening operacional | seguranca, observabilidade, auditoria e rollout |

---

## 4. Fase 01 - Fundacao de Produto e Dominio

### Task 1.1 - Consolidar arquitetura funcional
**Tempo estimado:** 4h  
**Descricao:** fechar o desenho funcional dos modulos `Brief Intake`, `Creative Queue`, `Production Pipeline`, `Review & Approval`, `Asset Library`, `Templates & Brand Systems`, `Delivery Center` e `Creative Analytics`.
**Verificacao:** mapa funcional aprovado e coerente com backend, frontend e HTML conceitual.

### Task 1.2 - Fechar taxonomia de demandas
**Tempo estimado:** 3h  
**Descricao:** definir tipos de demanda suportados no MVP e classificacoes-base por origem, canal, objetivo, urgencia, campanha, marca e tipo de entregavel.
**Verificacao:** tabela de taxonomia versionada e citada no backend/frontend.

### Task 1.3 - Fechar modelo conceitual de entidades
**Tempo estimado:** 4h  
**Descricao:** validar entidades centrais e complementares, com foco em `briefs`, `design_requests`, `creative_tasks`, `deliverables`, `asset_files`, `asset_versions`, `approval_steps`, `templates`, `brand_guidelines`, `design_collections` e tabelas de integracao.
**Verificacao:** ERD conceitual aprovado e consistente com PRD backend.

### Task 1.4 - Definir estados e transicoes
**Tempo estimado:** 3h  
**Descricao:** fechar estados de request, task, deliverable e approval, com regras de retrabalho, gates e transicoes validas.
**Verificacao:** matriz de status com transicoes validas documentada.

### Task 1.5 - Definir contratos de integracao FBR
**Tempo estimado:** 4h  
**Descricao:** especificar entradas e saidas iniciais para `FBR-Sales`, `FBR-MKT`, `FBR-Video`, `FBR-Redacao`, `FBR-Finance` e `FBR-Dev`.
**Verificacao:** lista de contratos MVP e backlog de contratos futuros.

---

## 5. Fase 02 - Backend Core

### Task 2.1 - Criar base de infraestrutura local/producao
**Tempo estimado:** 6h  
**Descricao:** preparar `docker-compose` com `postgres`, `redis`, `minio`, `backend`, `frontend`, `nginx`, `grafana` e `prometheus`.
**Verificacao:** stack sobe com `docker compose config` e servicos-base operacionais.

### Task 2.2 - Implementar schema inicial
**Tempo estimado:** 8h  
**Descricao:** criar schema SQL/Alembic com entidades de dominio, enums, constraints, chaves externas, soft delete onde aplicavel e audit trail imutavel.
**Verificacao:** migrations sobem sem erro e cobrem entidades do MVP.

### Task 2.3 - Implementar camada core
**Tempo estimado:** 8h  
**Descricao:** estruturar `config`, `database`, `security`, `storage`, `audit`, `events`, `auth` e politicas de permissao.
**Verificacao:** bootstrap backend funcional com healthcheck, conexao DB e sessao valida.

### Task 2.4 - Implementar modulos de dominio do MVP
**Tempo estimado:** 20h  
**Descricao:** desenvolver services e routers para:

- `briefs`
- `design_requests`
- `creative_tasks`
- `deliverables`
- `asset_files`
- `asset_versions`
- `feedback_threads`
- `approval_steps`
- `templates`
- `brand_guidelines`
- `design_collections`

**Verificacao:** CRUDs e operacoes de workflow funcionando em ambiente local.

### Task 2.5 - Implementar motor inicial de workflow
**Tempo estimado:** 10h  
**Descricao:** criar regras para intake, triagem, fila, producao, revisao, aprovacao, entrega e retrabalho, com suporte a blueprints simples por tipo de demanda.
**Verificacao:** request percorre pipeline completo sem perda de historico.

### Task 2.6 - Implementar versionamento e lineage
**Tempo estimado:** 8h  
**Descricao:** garantir upload em storage, checksum, derivacao entre versoes, definicao de versao final e lineage de reutilizacao.
**Verificacao:** deliverable possui historico navegavel e `final_version_id` consistente.

### Task 2.7 - Implementar auditoria e trilha operacional
**Tempo estimado:** 6h  
**Descricao:** registrar eventos-chave: criacao, reclassificacao, repriorizacao, atribuicao, feedback, aprovacao, rejeicao, entrega e arquivamento.
**Verificacao:** logs de auditoria aparecem para todas as acoes irreversiveis.

---

## 6. Fase 03 - Frontend Studio

### Task 3.1 - Criar shell visual do estudio
**Tempo estimado:** 8h  
**Descricao:** implementar layout principal com sidebar, topbar contextual, atmosfera editorial, identidade FBR e navegacao por dominio.
**Verificacao:** shell consistente com o PRD frontend e sem cara de dashboard generico.

### Task 3.2 - Implementar Overview
**Tempo estimado:** 8h  
**Descricao:** construir landing interna com volume da semana, backlog em risco, aprovacoes pendentes, campanhas ativas e reutilizacao recente.
**Verificacao:** overview comunica operacao e contexto executivo.

### Task 3.3 - Implementar Brief Intake
**Tempo estimado:** 12h  
**Descricao:** criar wizard de briefing com contexto, origem, objetivo, referencias, anexos, marca, campanha, restricoes e resumo final.
**Verificacao:** usuario abre uma demanda completa sem atrito e com validacao adequada.

### Task 3.4 - Implementar Requests e Request Detail
**Tempo estimado:** 14h  
**Descricao:** criar lista de demandas e pagina mestra da demanda com hero contextual, pipeline, deliverables, versoes, feedbacks e aprovacoes.
**Verificacao:** request pode ser acompanhada ponta a ponta pelo frontend.

### Task 3.5 - Implementar Queue e Production
**Tempo estimado:** 12h  
**Descricao:** desenvolver cockpit de fila com criticidade/SLA e visao de producao com foco em entregaveis e versoes.
**Verificacao:** equipe consegue priorizar e operar a fila criativa.

### Task 3.6 - Implementar Reviews e Delivery
**Tempo estimado:** 10h  
**Descricao:** criar central de revisao/aprovacao e centro de entrega com gates claros, CTA seguro e trilha de aceite.
**Verificacao:** aprovacao e pedido de ajustes funcionam com registro contextual.

### Task 3.7 - Implementar Library, Templates e Brands
**Tempo estimado:** 14h  
**Descricao:** desenvolver biblioteca navegavel, centro de templates e governanca visual de marcas.
**Verificacao:** ativos e sistemas visuais ficam localizaveis e reutilizaveis.

### Task 3.8 - Implementar Analytics inicial
**Tempo estimado:** 8h  
**Descricao:** construir indicadores de throughput, SLA, retrabalho, round de aprovacao, reutilizacao e origem FBR.
**Verificacao:** cockpit criativo inicial funcional.

---

## 7. Fase 04 - Integracoes FBR

### Task 4.1 - Integracao com FBR-Sales
**Tempo estimado:** 10h  
**Descricao:** receber demandas comerciais, campanhas, media kits, bundles e propostas; devolver status, entregaveis e ativos reutilizaveis.
**Verificacao:** contrato MVP de criativos comerciais testado.

### Task 4.2 - Integracao com FBR-MKT
**Tempo estimado:** 8h  
**Descricao:** suportar entrada de campanhas, posicionamento e branding; devolver kits visuais, timeline de aprovacao e outputs organizados.
**Verificacao:** campanha nasce em `FBR-MKT` e gera demanda rastreavel no `FBR-Design`.

### Task 4.3 - Integracao com FBR-Video e FBR-Redacao
**Tempo estimado:** 8h  
**Descricao:** permitir dependencias cruzadas entre roteiro/copy/video/design, com troca estruturada de insumos.
**Verificacao:** request consegue depender de copy ou identidade audiovisual sem fluxo manual disperso.

### Task 4.4 - Integracao com FBR-Finance
**Tempo estimado:** 6h  
**Descricao:** criar base para custo de producao externa, fornecedores e centro de custo por demanda.
**Verificacao:** request suporta metadados financeiros e trilha auditavel.

### Task 4.5 - Integracao com FBR-Dev
**Tempo estimado:** 8h  
**Descricao:** alinhar storage, automacoes, webhooks, busca, IA assistiva e futuras automacoes ecossistemicas.
**Verificacao:** contratos tecnicos com `FBR-Dev` documentados e testados.

---

## 8. Fase 05 - IA Assistiva e Organizacao Inteligente

### Task 5.1 - Assistencia ao briefing
**Tempo estimado:** 8h  
**Descricao:** sugerir classificacao, identificar lacunas, propor entregaveis e sinalizar risco de briefing fraco.
**Verificacao:** assistente retorna estrutura consistente sem substituir validacao humana.

### Task 5.2 - Assistencia a fila criativa
**Tempo estimado:** 8h  
**Descricao:** sugerir prioridade, risco de SLA, agrupamentos e dependencias provaveis.
**Verificacao:** sistema gera sinais operacionais uteis e auditaveis.

### Task 5.3 - Assistencia a biblioteca e reaproveitamento
**Tempo estimado:** 10h  
**Descricao:** indexar ativos, sugerir similares, apontar lineage e recomendar templates ou assets reutilizaveis.
**Verificacao:** novas demandas recebem recomendacoes relevantes de reutilizacao.

---

## 9. Fase 06 - Hardening e Go-Live

### Task 6.1 - Seguranca
**Tempo estimado:** 8h  
**Descricao:** revisar auth, autorizacao por role, sessao proxy, validacao de upload, webhooks assinados, CORS e sanitizacao de erros.
**Verificacao:** checklist de seguranca aprovado.

### Task 6.2 - Observabilidade
**Tempo estimado:** 6h  
**Descricao:** estruturar logs, metricas, dashboard de operacao e alertas.
**Verificacao:** Grafana/Prometheus mostram saude do sistema e gargalos.

### Task 6.3 - Testes integrados
**Tempo estimado:** 12h  
**Descricao:** validar fluxos ponta a ponta: intake -> queue -> production -> approval -> delivery -> library.
**Verificacao:** cenarios centrais do MVP passam sem regressao.

### Task 6.4 - Rollout controlado
**Tempo estimado:** 6h  
**Descricao:** liberar primeiro para um conjunto reduzido de marcas/projetos e coletar feedback operacional.
**Verificacao:** rollout inicial concluido com backlog de ajustes priorizado.

---

## 10. Ordem Recomendada de Execucao

1. Fundacao do dominio e contratos
2. Schema + backend core
3. Workflow + versionamento
4. Frontend studio MVP
5. Integracoes prioritarias com `FBR-Sales` e `FBR-MKT`
6. Library, templates e brands
7. Analytics
8. IA assistiva
9. Hardening e rollout

---

## 11. Backlog MVP vs Proxima Onda

### MVP

- intake
- requests
- queue
- production basica
- review and approval
- deliverables
- versionamento
- asset library inicial
- templates
- brands
- analytics inicial
- integracao prioritaria com `FBR-Sales` e `FBR-MKT`

### Proxima onda

- workflow blueprint avancado
- aprovacao paralela
- score de consistencia de marca
- sugestao inteligente de reaproveitamento
- custos e fornecedores completos
- cockpit executivo criativo
- automacoes ecossistemicas ampliadas

---

## 12. Criterios de Pronto

O `FBR-Design` pode ser considerado pronto para operacao inicial quando:

- recebe demandas de mais de um modulo FBR
- transforma briefing em pipeline rastreavel
- opera revisao e aprovacao sem perder historico
- versiona arquivos e entregaveis corretamente
- entrega outputs com lineage e biblioteca reutilizavel
- preserva governanca visual de marcas
- expone indicadores operacionais confiaveis
- sustenta a futura maturidade comercial do `FBR-Sales`

---

## 13. Resumo Executivo

Este plano reposiciona o `FBR-Design` como sistema real do ecossistema FBR. A implementacao deixa de ser orientada a "geracao automatica de pecas" e passa a ser orientada a operacao criativa empresarial: integrada, governada, versionada, reutilizavel e preparada para crescer junto com a maturidade dos demais modulos.
