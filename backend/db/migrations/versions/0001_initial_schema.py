"""initial schema

Revision ID: 0001_initial_schema
Revises: 
Create Date: 2026-03-14 11:30:00
"""

from alembic import op


revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
        CREATE EXTENSION IF NOT EXISTS pgcrypto;

        CREATE TYPE source_system_enum AS ENUM ('fbr_sales','fbr_mkt','fbr_video','fbr_redacao','fbr_click','fbr_leads','fbr_finance','fbr_dev','internal_manual');
        CREATE TYPE request_priority_enum AS ENUM ('low','medium','high','urgent');
        CREATE TYPE design_request_status_enum AS ENUM ('draft','submitted','triaged','queued','in_production','in_internal_review','in_stakeholder_approval','changes_requested','approved','delivered','archived','cancelled');
        CREATE TYPE creative_task_status_enum AS ENUM ('pending','ready','in_progress','blocked','in_review','done','cancelled');
        CREATE TYPE deliverable_status_enum AS ENUM ('not_started','draft_ready','review_ready','approval_pending','approved','delivered','superseded');
        CREATE TYPE approval_status_enum AS ENUM ('pending','open','approved','changes_requested','rejected','skipped');
        CREATE TYPE feedback_target_enum AS ENUM ('design_request','creative_task','deliverable','asset_version');
        CREATE TYPE deliverable_type_enum AS ENUM ('social_post','banner','presentation','media_kit','brand_asset','institutional_piece','thumbnail','campaign_kit','editorial_piece');

        CREATE OR REPLACE FUNCTION set_updated_at()
        RETURNS TRIGGER AS $$
        BEGIN
          NEW.updated_at = NOW();
          RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        CREATE TABLE projects (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          code VARCHAR(50) NOT NULL UNIQUE,
          name VARCHAR(150) NOT NULL,
          description TEXT,
          is_active BOOLEAN NOT NULL DEFAULT TRUE,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE TABLE brands (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          project_id UUID NOT NULL REFERENCES projects(id),
          parent_brand_id UUID REFERENCES brands(id),
          name VARCHAR(150) NOT NULL,
          slug VARCHAR(150) NOT NULL UNIQUE,
          status VARCHAR(30) NOT NULL DEFAULT 'active',
          primary_color VARCHAR(20),
          secondary_color VARCHAR(20),
          notes TEXT,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE campaigns (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          project_id UUID NOT NULL REFERENCES projects(id),
          brand_id UUID NOT NULL REFERENCES brands(id),
          source_system source_system_enum NOT NULL,
          source_reference_id VARCHAR(120),
          name VARCHAR(180) NOT NULL,
          objective TEXT,
          starts_at TIMESTAMPTZ,
          ends_at TIMESTAMPTZ,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE briefs (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          source_system source_system_enum NOT NULL,
          source_reference_id VARCHAR(120),
          project_id UUID NOT NULL REFERENCES projects(id),
          brand_id UUID NOT NULL REFERENCES brands(id),
          campaign_id UUID REFERENCES campaigns(id),
          requester_name VARCHAR(150) NOT NULL,
          requester_email VARCHAR(180),
          title VARCHAR(180) NOT NULL,
          objective TEXT NOT NULL,
          audience TEXT,
          channel VARCHAR(120),
          constraints TEXT,
          references_summary TEXT,
          ai_intake_notes TEXT,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE design_requests (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          brief_id UUID NOT NULL REFERENCES briefs(id),
          project_id UUID NOT NULL REFERENCES projects(id),
          brand_id UUID NOT NULL REFERENCES brands(id),
          campaign_id UUID REFERENCES campaigns(id),
          source_system source_system_enum NOT NULL,
          source_reference_id VARCHAR(120),
          request_type VARCHAR(80) NOT NULL,
          priority request_priority_enum NOT NULL,
          status design_request_status_enum NOT NULL,
          current_stage VARCHAR(80) NOT NULL,
          round_number INTEGER NOT NULL DEFAULT 1 CHECK (round_number >= 1),
          owner_team VARCHAR(80),
          assigned_lead_name VARCHAR(150),
          risk_level VARCHAR(30),
          sla_due_at TIMESTAMPTZ,
          requested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          approved_at TIMESTAMPTZ,
          delivered_at TIMESTAMPTZ,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE creative_tasks (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          design_request_id UUID NOT NULL REFERENCES design_requests(id),
          parent_task_id UUID REFERENCES creative_tasks(id),
          task_type VARCHAR(80) NOT NULL,
          title VARCHAR(180) NOT NULL,
          description TEXT,
          status creative_task_status_enum NOT NULL,
          assigned_to_name VARCHAR(150),
          depends_on_task_id UUID REFERENCES creative_tasks(id),
          started_at TIMESTAMPTZ,
          due_at TIMESTAMPTZ,
          completed_at TIMESTAMPTZ,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE deliverables (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          design_request_id UUID NOT NULL REFERENCES design_requests(id),
          deliverable_type deliverable_type_enum NOT NULL,
          name VARCHAR(180) NOT NULL,
          format VARCHAR(60) NOT NULL,
          channel VARCHAR(120),
          status deliverable_status_enum NOT NULL,
          delivery_channel VARCHAR(120),
          final_version_id UUID,
          approved_at TIMESTAMPTZ,
          delivered_at TIMESTAMPTZ,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE asset_files (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          design_request_id UUID REFERENCES design_requests(id),
          deliverable_id UUID REFERENCES deliverables(id),
          brand_id UUID REFERENCES brands(id),
          campaign_id UUID REFERENCES campaigns(id),
          name VARCHAR(180) NOT NULL,
          file_kind VARCHAR(60) NOT NULL,
          mime_group VARCHAR(40),
          tags TEXT,
          usage_context TEXT,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE asset_versions (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          asset_file_id UUID NOT NULL REFERENCES asset_files(id),
          version_number INTEGER NOT NULL,
          derived_from_version_id UUID REFERENCES asset_versions(id),
          storage_key VARCHAR(255) NOT NULL,
          storage_bucket VARCHAR(120) NOT NULL,
          mime_type VARCHAR(120) NOT NULL,
          file_size_bytes BIGINT NOT NULL,
          checksum VARCHAR(128) NOT NULL,
          origin_type VARCHAR(60) NOT NULL,
          change_summary TEXT,
          is_final BOOLEAN NOT NULL DEFAULT FALSE,
          approved_by_name VARCHAR(150),
          approved_at TIMESTAMPTZ,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          CONSTRAINT uq_asset_versions_asset_version UNIQUE (asset_file_id, version_number)
        );

        ALTER TABLE deliverables ADD CONSTRAINT fk_deliverables_final_version FOREIGN KEY (final_version_id) REFERENCES asset_versions(id);

        CREATE TABLE feedback_threads (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          target_type feedback_target_enum NOT NULL,
          target_id UUID NOT NULL,
          design_request_id UUID NOT NULL REFERENCES design_requests(id),
          status VARCHAR(30) NOT NULL DEFAULT 'open',
          title VARCHAR(180),
          created_by_name VARCHAR(150) NOT NULL,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE TABLE feedback_entries (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          thread_id UUID NOT NULL REFERENCES feedback_threads(id),
          author_name VARCHAR(150) NOT NULL,
          author_role VARCHAR(80),
          message TEXT NOT NULL,
          is_change_request BOOLEAN NOT NULL DEFAULT FALSE,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE TABLE approval_steps (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          target_type VARCHAR(40) NOT NULL,
          target_id UUID NOT NULL,
          design_request_id UUID NOT NULL REFERENCES design_requests(id),
          deliverable_id UUID REFERENCES deliverables(id),
          step_order INTEGER NOT NULL,
          step_name VARCHAR(120) NOT NULL,
          approver_role VARCHAR(80),
          approver_name VARCHAR(150),
          status approval_status_enum NOT NULL,
          decision_reason TEXT,
          due_at TIMESTAMPTZ,
          decided_at TIMESTAMPTZ,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          CONSTRAINT uq_approval_steps_target_order UNIQUE (target_type, target_id, step_order)
        );

        CREATE TABLE templates (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          project_id UUID REFERENCES projects(id),
          brand_id UUID REFERENCES brands(id),
          name VARCHAR(180) NOT NULL,
          slug VARCHAR(180) NOT NULL UNIQUE,
          template_type VARCHAR(80) NOT NULL,
          channel VARCHAR(120),
          description TEXT,
          preview_asset_file_id UUID REFERENCES asset_files(id),
          status VARCHAR(30) NOT NULL DEFAULT 'active',
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE brand_guidelines (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          brand_id UUID NOT NULL REFERENCES brands(id),
          version_label VARCHAR(60) NOT NULL,
          status VARCHAR(30) NOT NULL DEFAULT 'draft',
          summary TEXT,
          rules_text TEXT,
          cover_asset_file_id UUID REFERENCES asset_files(id),
          published_at TIMESTAMPTZ,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
          deleted_at TIMESTAMPTZ
        );

        CREATE TABLE audit_logs (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          entity_type VARCHAR(80) NOT NULL,
          entity_id UUID NOT NULL,
          action VARCHAR(80) NOT NULL,
          actor_name VARCHAR(150),
          actor_role VARCHAR(80),
          metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE INDEX idx_design_requests_status_priority_sla ON design_requests (status, priority, sla_due_at);
        CREATE INDEX idx_design_requests_project_brand_campaign ON design_requests (project_id, brand_id, campaign_id);
        CREATE INDEX idx_creative_tasks_request_status_due ON creative_tasks (design_request_id, status, due_at);
        CREATE INDEX idx_deliverables_request_status ON deliverables (design_request_id, status);
        CREATE INDEX idx_approval_steps_status_due ON approval_steps (status, due_at);
        CREATE INDEX idx_asset_versions_asset_file_version ON asset_versions (asset_file_id, version_number DESC);
        CREATE INDEX idx_templates_brand_type_status ON templates (brand_id, template_type, status);
        CREATE INDEX idx_asset_files_brand_campaign ON asset_files (brand_id, campaign_id);
        CREATE INDEX idx_audit_logs_entity_created ON audit_logs (entity_type, entity_id, created_at DESC);

        CREATE TRIGGER trg_projects_updated_at BEFORE UPDATE ON projects FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_brands_updated_at BEFORE UPDATE ON brands FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_campaigns_updated_at BEFORE UPDATE ON campaigns FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_briefs_updated_at BEFORE UPDATE ON briefs FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_design_requests_updated_at BEFORE UPDATE ON design_requests FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_creative_tasks_updated_at BEFORE UPDATE ON creative_tasks FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_deliverables_updated_at BEFORE UPDATE ON deliverables FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_asset_files_updated_at BEFORE UPDATE ON asset_files FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_feedback_threads_updated_at BEFORE UPDATE ON feedback_threads FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_approval_steps_updated_at BEFORE UPDATE ON approval_steps FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_templates_updated_at BEFORE UPDATE ON templates FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        CREATE TRIGGER trg_brand_guidelines_updated_at BEFORE UPDATE ON brand_guidelines FOR EACH ROW EXECUTE FUNCTION set_updated_at();
        """
    )


def downgrade() -> None:
    op.execute(
        """
        DROP TRIGGER IF EXISTS trg_brand_guidelines_updated_at ON brand_guidelines;
        DROP TRIGGER IF EXISTS trg_templates_updated_at ON templates;
        DROP TRIGGER IF EXISTS trg_approval_steps_updated_at ON approval_steps;
        DROP TRIGGER IF EXISTS trg_feedback_threads_updated_at ON feedback_threads;
        DROP TRIGGER IF EXISTS trg_asset_files_updated_at ON asset_files;
        DROP TRIGGER IF EXISTS trg_deliverables_updated_at ON deliverables;
        DROP TRIGGER IF EXISTS trg_creative_tasks_updated_at ON creative_tasks;
        DROP TRIGGER IF EXISTS trg_design_requests_updated_at ON design_requests;
        DROP TRIGGER IF EXISTS trg_briefs_updated_at ON briefs;
        DROP TRIGGER IF EXISTS trg_campaigns_updated_at ON campaigns;
        DROP TRIGGER IF EXISTS trg_brands_updated_at ON brands;
        DROP TRIGGER IF EXISTS trg_projects_updated_at ON projects;

        DROP TABLE IF EXISTS audit_logs;
        DROP TABLE IF EXISTS brand_guidelines;
        DROP TABLE IF EXISTS templates;
        DROP TABLE IF EXISTS approval_steps;
        DROP TABLE IF EXISTS feedback_entries;
        DROP TABLE IF EXISTS feedback_threads;
        DROP TABLE IF EXISTS asset_versions;
        DROP TABLE IF EXISTS asset_files;
        DROP TABLE IF EXISTS deliverables;
        DROP TABLE IF EXISTS creative_tasks;
        DROP TABLE IF EXISTS design_requests;
        DROP TABLE IF EXISTS briefs;
        DROP TABLE IF EXISTS campaigns;
        DROP TABLE IF EXISTS brands;
        DROP TABLE IF EXISTS projects;

        DROP FUNCTION IF EXISTS set_updated_at;
        DROP TYPE IF EXISTS deliverable_type_enum;
        DROP TYPE IF EXISTS feedback_target_enum;
        DROP TYPE IF EXISTS approval_status_enum;
        DROP TYPE IF EXISTS deliverable_status_enum;
        DROP TYPE IF EXISTS creative_task_status_enum;
        DROP TYPE IF EXISTS design_request_status_enum;
        DROP TYPE IF EXISTS request_priority_enum;
        DROP TYPE IF EXISTS source_system_enum;
        """
    )
