"""add collection_id foreign key

Revision ID: 7486775ac006
Revises: 1aeeb4735fc1
Create Date: 2023-06-05 21:40:54.512660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7486775ac006'
down_revision = '1aeeb4735fc1'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE collections_items
        ADD CONSTRAINT fk_ci_collections
        FOREIGN KEY (collection_id)
        REFERENCES collections
        ON DELETE CASCADE;
        """
    )


def downgrade():
    op.execute(
        """
       ALTER TABLE collections_items
            DROP CONSTRAINT fk_ci_collections;
       """
    )
