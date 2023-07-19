"""insert collections values

Revision ID: 07e902be0545
Revises: f2fdff85b41c
Create Date: 2023-06-05 22:24:21.548791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07e902be0545'
down_revision = 'f2fdff85b41c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO collections (name, user_id)
        VALUES ('Home', 1);
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM collections
        WHERE name = 'Home';
        """
    )
