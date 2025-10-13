"""add content column

Revision ID: b9c584f5a7f8
Revises: 0efc8d0192bf
Create Date: 2025-10-13 14:08:07.727456

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9c584f5a7f8'
down_revision: Union[str, None] = '0efc8d0192bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
