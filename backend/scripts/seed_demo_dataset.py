import os

from sqlalchemy import create_engine, text

PROJECT_ID = "11111111-1111-1111-1111-111111111111"
BRAND_ID = "22222222-2222-2222-2222-222222222222"
CAMPAIGN_ID = "33333333-3333-3333-3333-333333333333"


def main() -> None:
    database_url = os.environ.get("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/fbr_design")
    sync_database_url = database_url.replace("+asyncpg", "+psycopg2")
    engine = create_engine(sync_database_url)

    with engine.begin() as connection:
        connection.execute(
            text(
                """
                INSERT INTO projects (id, code, name, description, is_active)
                VALUES (:id, :code, :name, :description, TRUE)
                ON CONFLICT (id) DO UPDATE SET
                  code = EXCLUDED.code,
                  name = EXCLUDED.name,
                  description = EXCLUDED.description,
                  is_active = EXCLUDED.is_active
                """
            ),
            {
                "id": PROJECT_ID,
                "code": "facebrasil",
                "name": "Facebrasil",
                "description": "Projeto base para ambiente local do FBR-Design.",
            },
        )

        connection.execute(
            text(
                """
                INSERT INTO brands (id, project_id, parent_brand_id, name, slug, status, primary_color, secondary_color, notes)
                VALUES (:id, :project_id, NULL, :name, :slug, :status, :primary_color, :secondary_color, :notes)
                ON CONFLICT (id) DO UPDATE SET
                  project_id = EXCLUDED.project_id,
                  name = EXCLUDED.name,
                  slug = EXCLUDED.slug,
                  status = EXCLUDED.status,
                  primary_color = EXCLUDED.primary_color,
                  secondary_color = EXCLUDED.secondary_color,
                  notes = EXCLUDED.notes
                """
            ),
            {
                "id": BRAND_ID,
                "project_id": PROJECT_ID,
                "name": "Facebrasil",
                "slug": "facebrasil",
                "status": "active",
                "primary_color": "#f97316",
                "secondary_color": "#08111f",
                "notes": "Brand seed do ambiente local.",
            },
        )

        connection.execute(
            text(
                """
                INSERT INTO campaigns (id, project_id, brand_id, source_system, source_reference_id, name, objective)
                VALUES (:id, :project_id, :brand_id, CAST(:source_system AS source_system_enum), :source_reference_id, :name, :objective)
                ON CONFLICT (id) DO UPDATE SET
                  project_id = EXCLUDED.project_id,
                  brand_id = EXCLUDED.brand_id,
                  source_system = EXCLUDED.source_system,
                  source_reference_id = EXCLUDED.source_reference_id,
                  name = EXCLUDED.name,
                  objective = EXCLUDED.objective
                """
            ),
            {
                "id": CAMPAIGN_ID,
                "project_id": PROJECT_ID,
                "brand_id": BRAND_ID,
                "source_system": "internal_manual",
                "source_reference_id": "seed-local-001",
                "name": "Campanha Base Local",
                "objective": "Suportar o fluxo inicial do MVP no ambiente local.",
            },
        )

    print("Demo dataset seeded successfully.")


if __name__ == "__main__":
    main()