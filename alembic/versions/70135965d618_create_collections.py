"""create collections

Revision ID: 70135965d618
Revises: 1f88f83f6df9
Create Date: 2023-06-05 21:11:38.078709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70135965d618'
down_revision = '1f88f83f6df9'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE collections(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            user_id INT NOT NULL 
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE collections;
        """
    )
