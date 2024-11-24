"""create storage and project tables

Revision ID: 3dd9d580a1a7
Revises: 46d673c6de55
Create Date: 2024-11-24 16:37:39.308401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dd9d580a1a7'
down_revision: Union[str, None] = '46d673c6de55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
