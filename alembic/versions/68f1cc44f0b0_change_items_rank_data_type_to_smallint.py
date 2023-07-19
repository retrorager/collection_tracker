"""change items rank data type to smallint

Revision ID: 68f1cc44f0b0
Revises: 173525655312
Create Date: 2023-06-10 10:56:32.373835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68f1cc44f0b0'
down_revision = '173525655312'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE items
        ALTER COLUMN rank TYPE SMALLINT;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE items
        ALTER COLUMN rank TYPE INT;
        """
    )
