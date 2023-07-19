"""create users

Revision ID: 1f88f83f6df9
Revises: 
Create Date: 2023-06-05 18:22:05.458884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f88f83f6df9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE users(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT UNIQUE
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE users;
        """
    )
