"""create initial tables

Revision ID: 4abef1ddb4c2
Revises:
Create Date: 2024-10-07 19:41:00.176211

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4abef1ddb4c2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "position",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("fen", sa.String(63), nullable=False),
        sa.Column("eval", sa.Float),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("fen"),
    )

    op.create_table(
        "game",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("description", sa.String(255), nullable=False),
        sa.Column("opening", sa.String(255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "game_position",
        sa.Column("game_id", sa.Integer, nullable=False),
        sa.Column("position_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(
            ["game_id"],
            ["game.id"],
        ),
        sa.ForeignKeyConstraint(
            ["position_id"],
            ["position.id"],
        ),
        sa.PrimaryKeyConstraint("game_id", "position_id"),
    )


def downgrade() -> None:
    op.drop_table("game_position")
    op.drop_table("position")
    op.drop_table("game")
