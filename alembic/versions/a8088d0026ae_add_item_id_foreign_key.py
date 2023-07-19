"""add item_id foreign key

Revision ID: a8088d0026ae
Revises: 7486775ac006
Create Date: 2023-06-05 21:46:38.393703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8088d0026ae'
down_revision = '7486775ac006'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE collections_items
        ADD CONSTRAINT fk_ci_items
        FOREIGN KEY (item_id)
        REFERENCES items
        ON DELETE CASCADE;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE collections_items
            DROP CONSTRAINT fk_ci_items;
        """
    )
