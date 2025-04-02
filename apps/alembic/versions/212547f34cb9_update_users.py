"""update users

Revision ID: 212547f34cb9
Revises: 21c02549fa19
Create Date: 2025-04-02 21:00:16.499947

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = "212547f34cb9"
down_revision: Union[str, None] = "21c02549fa19"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="True"),
    )
    op.add_column(
        "users",
        sa.Column(
            "is_superuser",
            sa.Boolean(),
            nullable=False,
            server_default="FALSE",  # 手动设置默认值
        ),
    )
    op.drop_column("users", "is_delete")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("is_delete", sa.BOOLEAN(), autoincrement=False, nullable=True),
    )
    op.drop_column("users", "is_superuser")
    op.drop_column("users", "is_active")
    # ### end Alembic commands ###
