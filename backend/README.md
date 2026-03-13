# Backend Bootstrap - FBR-Design

Estrutura inicial do backend do `FBR-Design`.

## Pastas

- `app/api/routers`: endpoints REST
- `app/core`: config, database, seguranca e utilitarios
- `app/models`: modelos ORM
- `app/schemas`: contratos Pydantic
- `app/services`: regras de negocio
- `db/schema.sql`: schema inicial PostgreSQL
- `db/migrations`: migrations Alembic

## Proximo passo sugerido

1. criar `app/main.py`
2. configurar `settings` e conexao SQLAlchemy
3. transformar `db/schema.sql` em migrations versionadas
