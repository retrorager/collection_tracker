"""create items

Revision ID: 381f7e681186
Revises: 70135965d618
Create Date: 2023-06-05 21:19:31.836973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '381f7e681186'
down_revision = '70135965d618'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE items(
            id SERIAL PRIMARY KEY,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            rank SMALLINT NOT NULL CHECK (rank BETWEEN 1 AND 5),
            format TEXT,
            genre TEXT,
            platform TEXT,
            author TEXT,
            max_players SMALLINT
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE items;
        """
    )
