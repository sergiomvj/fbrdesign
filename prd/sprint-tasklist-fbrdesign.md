# Sprint Tasklist - FBR-Design
> Tracker de execucao da sprint autonoma de documentacao e concepcao.
> Atualizar este arquivo conforme os blocos forem concluidos.

**Status geral:** sprint tecnica em andamento  
**Foco atual:** a espinha dorsal do request detail do MVP esta praticamente completa; o proximo salto e consolidar migrations reais e acoes mutativas

---

## Objetivo da Sprint

Consolidar o `FBR-Design` como sistema real do ecossistema FBR, com documentacao coerente entre produto, backend, frontend, plano de implementacao e apresentacao conceitual.

---

## Progresso Tecnico Atual

- [x] Schema relacional inicial definido em documento
- [x] Contratos REST do MVP definidos
- [x] Workflow e transicoes detalhados
- [x] Mapa inicial de telas definido
- [x] Backlog tecnico organizado
- [x] `backend/db/schema.sql` criado
- [x] Estrutura base de `backend/` e `frontend/` criada
- [x] Bootstrap minimo do backend iniciado
- [x] Bootstrap minimo do frontend iniciado
- [x] Dominios `briefs`, `design_requests`, `deliverables`, `approval_steps`, `feedback_threads` e `asset_versions` iniciados em codigo
- [x] Tipos TypeScript e `fetcher` base criados
- [x] Páginas P0 ligadas a dados tipados com fallback mock
- [x] Alembic iniciado em nivel de bootstrap

---

## Registro de Progresso

### 2026-03-13

- [x] Sprint documental concluida
- [x] `implementation-plan-fbrdesign.md` reescrito
- [x] `prd-backend-fbrdesign.md` reescrito
- [x] `prd-frontend-fbrdesign.md` reescrito
- [x] `index.html` reconstruido

### 2026-03-14

- [x] `schema-relacional-inicial-fbrdesign.md` criado
- [x] `api-contracts-mvp-fbrdesign.md` criado
- [x] `backlog-tecnico-mvp-fbrdesign.md` criado
- [x] `workflow-transicoes-mvp-fbrdesign.md` criado
- [x] `mapa-telas-approuter-fbrdesign.md` criado
- [x] `backend/db/schema.sql` criado
- [x] estrutura inicial de `backend/` criada
- [x] estrutura inicial de `frontend/` criada
- [x] `README.md` raiz criado
- [x] `backend/README.md` criado
- [x] `frontend/README.md` criado
- [x] `backend/app/main.py` criado
- [x] `backend/app/core/config.py` criado
- [x] `backend/app/core/database.py` criado
- [x] `backend/app/api/routers/health.py` criado
- [x] `backend/app/models/project.py` criado
- [x] `backend/app/schemas/common.py` criado
- [x] `backend/requirements.txt` criado
- [x] `python -m compileall backend/app` executado com sucesso
- [x] `frontend/package.json` criado
- [x] `frontend/tsconfig.json` criado
- [x] `frontend/app/layout.tsx` criado
- [x] `frontend/app/globals.css` criado
- [x] `frontend/app/(studio)/layout.tsx` criado
- [x] `frontend/app/(studio)/page.tsx` criado
- [x] rotas P0 iniciais (`/intake`, `/requests`, `/reviews`) criadas
- [x] `backend/app/models/brief.py` criado
- [x] `backend/app/models/design_request.py` criado
- [x] `backend/app/models/enums.py` criado
- [x] `backend/app/schemas/brief.py` criado
- [x] `backend/app/schemas/design_request.py` criado
- [x] `backend/app/api/routers/briefs.py` criado
- [x] `backend/app/api/routers/design_requests.py` criado
- [x] `frontend/types/brief.ts` criado
- [x] `frontend/types/design-request.ts` criado
- [x] `frontend/lib/fetcher.ts` criado
- [x] `frontend/lib/api.ts` criado
- [x] `frontend/components/studio/StatusBadge.tsx` criado
- [x] `frontend/app/(studio)/requests/[id]/page.tsx` criado
- [x] `frontend/app/api/briefs/route.ts` criado
- [x] `frontend/app/api/design-requests/route.ts` criado
- [x] `frontend/app/(studio)/requests/page.tsx` ligado a dados tipados
- [x] `frontend/app/(studio)/intake/page.tsx` ligado a dados tipados
- [x] `frontend/app/(studio)/reviews/page.tsx` ligado a dados tipados
- [x] `frontend/tsconfig.json` ajustado com alias `@/*`
- [x] `backend/alembic.ini` criado
- [x] `backend/db/migrations/env.py` criado
- [x] `backend/db/migrations/script.py.mako` criado
- [x] `backend/db/migrations/versions/0001_initial_schema.py` criado
- [x] `backend/app/models/brand.py` criado
- [x] `backend/app/models/campaign.py` criado
- [x] `backend/app/models/deliverable.py` criado
- [x] `backend/app/models/approval_step.py` criado
- [x] `backend/app/models/feedback_thread.py` criado
- [x] `backend/app/models/asset_version.py` criado
- [x] `backend/app/schemas/deliverable.py` criado
- [x] `backend/app/schemas/approval_step.py` criado
- [x] `backend/app/schemas/feedback_thread.py` criado
- [x] `backend/app/schemas/asset_version.py` criado
- [x] `backend/app/api/routers/deliverables.py` criado
- [x] `backend/app/api/routers/approval_steps.py` criado
- [x] `backend/app/api/routers/feedback_threads.py` criado
- [x] `backend/app/api/routers/asset_versions.py` criado
- [x] `frontend/types/deliverable.ts` criado
- [x] `frontend/types/approval-step.ts` criado
- [x] `frontend/types/feedback-thread.ts` criado
- [x] `frontend/types/asset-version.ts` criado
- [x] `frontend/app/api/deliverables/route.ts` criado
- [x] `frontend/app/api/approval-steps/route.ts` criado
- [x] `frontend/app/api/feedback-threads/route.ts` criado
- [x] `frontend/app/api/asset-versions/route.ts` criado
- [x] `frontend/lib/api.ts` expandido com detail agregado
- [x] `frontend/app/(studio)/requests/[id]/page.tsx` enriquecido com briefing, deliverables, approval gates, feedback threads e versions
- [x] `python -m compileall backend/app` reexecutado com sucesso apos expansoes

---

## Proximo Bloco Recomendado

- [ ] substituir migration placeholder por migration real
- [ ] iniciar acoes mutativas no frontend para requests/approvals
- [ ] adicionar `feedback_entries` e `creative_tasks`
- [ ] preparar stack local para subir e testar ponta a ponta

---

## Observacoes

- O tool `apply_patch` apresentou falha interna do sandbox nesta sessao; por isso, a ultima rodada de criacao de arquivos foi feita via PowerShell para nao interromper o andamento.
- O request detail ja esta muito mais proximo de uma tela mestra real do que de um placeholder conceitual.
