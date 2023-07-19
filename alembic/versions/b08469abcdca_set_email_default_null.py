"""set email default null

Revision ID: b08469abcdca
Revises: a5d54e6d39c2
Create Date: 2023-06-07 18:27:56.970017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b08469abcdca'
down_revision = 'a5d54e6d39c2'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN email
        SET DEFAULT NULL;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN email
        DROP DEFAULT;
        """
    )
