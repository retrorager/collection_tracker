"""create collections_items

Revision ID: 765399f4044c
Revises: 381f7e681186
Create Date: 2023-06-05 21:27:23.288941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '765399f4044c'
down_revision = '381f7e681186'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE collections_items(
            collection_id INT NOT NULL,
            item_id INT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE collections_items;
        """
    )
