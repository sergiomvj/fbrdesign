# Sprint Tasklist - FBR-Design
> Tracker de execucao da sprint autonoma de documentacao e concepcao.
> Atualizar este arquivo conforme os blocos forem concluidos.

**Status geral:** sprint tecnica em andamento  
**Foco atual:** stack local operacional, fluxo central validado e proximo salto em dados ricos de producao

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
- [x] Dominios centrais do MVP iniciados em codigo
- [x] Tipos TypeScript e `fetcher` base criados
- [x] Páginas P0 ligadas a dados tipados com fallback mock
- [x] Alembic iniciado com migration inicial real
- [x] Stack local configurada com `docker-compose.yml`
- [x] Primeira acao mutativa do frontend implementada (`create briefing`)
- [x] Intake agora consegue abrir `briefing + design_request` no mesmo fluxo
- [x] Request detail agora permite decidir `approval_steps` pela interface
- [x] IDs default do frontend alinhados para UUID valido no caminho do backend real
- [x] `npm run typecheck` executado com sucesso
- [x] `python -m compileall backend/app` executado com sucesso
- [x] Stack local subida com sucesso em portas alternativas (`3541`, `8541`, `5543`)
- [x] Healthcheck real do backend respondendo `ok`
- [x] Seed local de entidades-base criado e executado
- [x] Criacao real de `brief` e `design_request` validada contra backend/postgres
- [x] Frontend containerizado respondendo e exibindo `requests` reais do backend

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
- [x] `docker-compose.yml` criado
- [x] `docker compose config` validou com sucesso
- [x] `backend/Dockerfile` criado
- [x] `frontend/Dockerfile` criado
- [x] `backend/.env.example` criado
- [x] `frontend/.env.example` criado
- [x] `backend/.dockerignore` criado
- [x] `frontend/.dockerignore` criado
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
- [x] `backend/app/models/brand.py` criado
- [x] `backend/app/models/campaign.py` criado
- [x] `backend/app/models/brief.py` criado
- [x] `backend/app/models/design_request.py` criado
- [x] `backend/app/models/creative_task.py` criado
- [x] `backend/app/models/deliverable.py` criado
- [x] `backend/app/models/approval_step.py` criado
- [x] `backend/app/models/feedback_thread.py` criado
- [x] `backend/app/models/feedback_entry.py` criado
- [x] `backend/app/models/asset_version.py` criado
- [x] `backend/app/models/db_enum.py` criado
- [x] `backend/app/models/enums.py` consolidado
- [x] enums do ORM alinhados com enums nativos do PostgreSQL
- [x] `backend/app/schemas/common.py` criado
- [x] `backend/app/schemas/brief.py` criado
- [x] `backend/app/schemas/design_request.py` criado
- [x] `backend/app/schemas/creative_task.py` criado
- [x] `backend/app/schemas/deliverable.py` criado
- [x] `backend/app/schemas/approval_step.py` criado
- [x] `backend/app/schemas/feedback_thread.py` criado
- [x] `backend/app/schemas/feedback_entry.py` criado
- [x] `backend/app/schemas/asset_version.py` criado
- [x] `backend/app/api/routers/briefs.py` criado
- [x] `backend/app/api/routers/design_requests.py` criado
- [x] `backend/app/api/routers/creative_tasks.py` criado
- [x] `backend/app/api/routers/deliverables.py` criado
- [x] `backend/app/api/routers/approval_steps.py` criado
- [x] `backend/app/api/routers/feedback_threads.py` criado
- [x] `backend/app/api/routers/feedback_entries.py` criado
- [x] `backend/app/api/routers/asset_versions.py` criado
- [x] `backend/alembic.ini` criado
- [x] `backend/db/migrations/env.py` criado
- [x] `backend/db/migrations/script.py.mako` criado
- [x] `backend/db/migrations/versions/0001_initial_schema.py` convertido em migration real
- [x] `backend/requirements.txt` atualizado com dependencias reais da stack local
- [x] `backend/scripts/seed_demo_dataset.py` criado
- [x] `backend` agora sobe com `alembic upgrade head` antes do `uvicorn`
- [x] `python -m compileall backend/app` executado com sucesso varias vezes
- [x] `python -m compileall backend/scripts` executado com sucesso
- [x] `frontend/package.json` ajustado para UTF-8 sem BOM
- [x] `frontend/tsconfig.json` ajustado para UTF-8 sem BOM e compatibilidade do Next
- [x] `frontend/package.json` criado
- [x] `frontend/app/layout.tsx` criado
- [x] `frontend/app/globals.css` criado
- [x] `frontend/app/(studio)/layout.tsx` criado
- [x] `frontend/app/(studio)/page.tsx` criado
- [x] rotas P0 iniciais (`/intake`, `/requests`, `/reviews`) criadas
- [x] `frontend/types/brief.ts` criado
- [x] `frontend/types/design-request.ts` criado
- [x] `frontend/types/creative-task.ts` criado
- [x] `frontend/types/deliverable.ts` criado
- [x] `frontend/types/approval-step.ts` criado
- [x] `frontend/types/feedback-thread.ts` criado
- [x] `frontend/types/feedback-entry.ts` criado
- [x] `frontend/types/asset-version.ts` criado
- [x] `frontend/lib/fetcher.ts` criado
- [x] `frontend/lib/api.ts` expandido para detail agregado amplo
- [x] `frontend/lib/studio-defaults.ts` criado
- [x] `frontend/components/studio/StatusBadge.tsx` criado
- [x] `frontend/components/studio/BriefIntakeForm.tsx` evoluido para abrir briefing e request
- [x] `frontend/components/studio/ApprovalActions.tsx` criado
- [x] `frontend/app/api/briefs/route.ts` ganhou `POST`
- [x] `frontend/app/api/design-requests/route.ts` ganhou `POST`
- [x] `frontend/app/api/design-requests/[id]/route.ts` criado com `PATCH`
- [x] `frontend/app/api/creative-tasks/route.ts` criado
- [x] `frontend/app/api/deliverables/route.ts` criado
- [x] `frontend/app/api/approval-steps/route.ts` ganhou `POST`
- [x] `frontend/app/api/approval-steps/[id]/route.ts` criado com `PATCH`
- [x] `frontend/app/api/feedback-threads/route.ts` criado
- [x] `frontend/app/api/feedback-entries/route.ts` criado
- [x] `frontend/app/api/asset-versions/route.ts` criado
- [x] `frontend/app/(studio)/requests/page.tsx` ligado a dados tipados
- [x] `frontend/app/(studio)/intake/page.tsx` ligado a dados tipados e com create briefing/request
- [x] `frontend/app/(studio)/reviews/page.tsx` evoluido para approval inbox por gates
- [x] `frontend/app/(studio)/requests/[id]/page.tsx` evoluido para tela mestra inicial com acoes de approval
- [x] `frontend/tsconfig.json` ajustado com alias `@/*`
- [x] `npm.cmd install` executado com sucesso
- [x] `python -m pip install -r backend/requirements.txt` executado com sucesso
- [x] `npm run typecheck` executado com sucesso
- [x] `docker compose up -d --build` concluido com sucesso
- [x] `docker compose exec -T backend python scripts/seed_demo_dataset.py` executado com sucesso
- [x] `GET /api/health` validado em `http://localhost:8541`
- [x] `POST /api/briefs` validado com sucesso
- [x] `POST /api/design-requests` validado com sucesso
- [x] `GET /requests` validado no frontend em `http://localhost:3541/requests`

---

## Proximo Bloco Recomendado

- [ ] adicionar seed mais rico com `creative_tasks`, `deliverables`, `approval_steps`, `feedback_threads` e `asset_versions`
- [ ] ligar `requests/[id]` totalmente a dados reais do banco em vez de depender de placeholders visuais
- [ ] adicionar acoes mutativas para `creative_tasks`, `feedback_entries` e `deliverables`
- [ ] revisar aderencia completa entre ORM atual, `schema.sql` e migration inicial
- [ ] iniciar camada de autenticacao/perfis internos e governanca por papel

---

## Observacoes

- O tool `apply_patch` apresentou falha interna do sandbox nesta sessao; por isso, a ultima rodada de criacao de arquivos foi feita via PowerShell para nao interromper o andamento.
- A stack local esta rodando nas portas `3541` (frontend), `8541` (backend) e `5543` (postgres) para evitar conflitos com outros projetos da maquina.
- O projeto ja deixou de ser apenas planejamento: ele agora tem stack local operacional, migration aplicada, seed local, healthcheck real, frontend no ar e fluxo central validado contra banco real.