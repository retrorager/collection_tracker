"""add btree index on items rank

Revision ID: b214ee2b8a47
Revises: b08469abcdca
Create Date: 2023-06-10 10:40:38.456793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b214ee2b8a47'
down_revision = 'b08469abcdca'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE INDEX items_rank_index ON items (rank); 
        """
    )


def downgrade():
    op.execute(
        """
        DROP INDEX items_rank_index;
        """
    )
