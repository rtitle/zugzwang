"""create games table

Revision ID: 991b06dbe96b
Revises:
Create Date: 2024-10-06 16:19:50.396060

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "991b06dbe96b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "games",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("white", sa.String(50), nullable=False),
        sa.Column("black", sa.String(50), nullable=False),
        sa.Column("white_elo", sa.Integer, nullable=False),
        sa.Column("black_elo", sa.Integer, nullable=False),
        sa.Column("opening", sa.String(1024)),
    )


def downgrade() -> None:
    op.drop_table("games")
