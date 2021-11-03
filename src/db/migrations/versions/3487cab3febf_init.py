# -*- coding: utf-8 -*-
"""Init

Revision ID: 3487cab3febf
Revises:
Create Date: 2021-11-03 18:00:25.288281

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "3487cab3febf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    op.execute("CREATE SCHEMA IF NOT EXISTS geo;")


def downgrade():
    op.execute("DROP SCHEMA IF EXISTS geo CASCADE;")
    op.execute("DROP EXTENSION IF EXISTS postgis CASCADE;")
