"""insert users values

Revision ID: f2fdff85b41c
Revises: a8088d0026ae
Create Date: 2023-06-05 22:14:53.841117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2fdff85b41c'
down_revision = 'a8088d0026ae'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO users (name, password, email)
        VALUES ('Evan', 'test1pass', 'e@email.com');
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM users
        WHERE name = 'Evan';
        """
    )
