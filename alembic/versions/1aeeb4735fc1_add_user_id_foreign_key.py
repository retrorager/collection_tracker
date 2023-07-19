"""add user_id foreign key

Revision ID: 1aeeb4735fc1
Revises: 765399f4044c
Create Date: 2023-06-05 21:30:19.480380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1aeeb4735fc1'
down_revision = '765399f4044c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE collections
        ADD CONSTRAINT fk_collections_users
        FOREIGN KEY (user_id)
        REFERENCES users
        ON DELETE CASCADE;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE collections
            DROP CONSTRAINT fk_collections_users;
        """
    )
