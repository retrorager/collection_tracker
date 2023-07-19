"""add hash index on items category

Revision ID: 173525655312
Revises: b214ee2b8a47
Create Date: 2023-06-10 10:53:15.622774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '173525655312'
down_revision = 'b214ee2b8a47'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE INDEX items_category_index ON items USING HASH (category); 
        """
    )


def downgrade():
    op.execute(
        """
        DROP INDEX items_category_index;
        """
    )