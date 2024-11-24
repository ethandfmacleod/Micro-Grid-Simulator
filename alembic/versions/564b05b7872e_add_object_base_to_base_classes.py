"""add object base to base classes

Revision ID: 564b05b7872e
Revises: 3dd9d580a1a7
Create Date: 2024-11-24 17:26:27.799303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '564b05b7872e'
down_revision: Union[str, None] = '3dd9d580a1a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
