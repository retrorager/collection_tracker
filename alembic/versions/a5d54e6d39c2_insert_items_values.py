"""insert items values

Revision ID: a5d54e6d39c2
Revises: 07e902be0545
Create Date: 2023-06-05 22:27:53.391058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5d54e6d39c2'
down_revision = '07e902be0545'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO items (category, title, rank, format, genre, platform, author, max_players)
        VALUES ('Video Game', 'Returnal', 5, 'Digital', 'Action', 'PS5', 'Sony', 2);
        """
    )


def downgrade():
    op.execute(
        """
        DELETE FROM items
        WHERE title = 'Returnal';
        """
    )
