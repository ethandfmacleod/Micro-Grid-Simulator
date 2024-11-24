"""Add EnergyOut

Revision ID: 46d673c6de55
Revises: 441d693760c0
Create Date: 2024-11-17 16:22:57.599031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '46d673c6de55'
down_revision: Union[str, None] = '441d693760c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('SolarPanels')
    op.drop_table('WindTurbines')
    op.drop_table('EnergyIns')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('EnergyIns',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"EnergyIns_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('watts', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('daily_emissions', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('type', postgresql.ENUM('Default', 'SolarPanel', 'WindTurbine', name='energyintype'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='EnergyIns_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('WindTurbines',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('rotor_diameter', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('rotation', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cut_in_speed', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('rated_speed', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cut_off_speed', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['EnergyIns.id'], name='WindTurbines_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='WindTurbines_pkey')
    )
    op.create_table('SolarPanels',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('panel_type', postgresql.ENUM('Default', name='solarpaneltype'), autoincrement=False, nullable=False),
    sa.Column('width', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('length', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('cells', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('material', postgresql.ENUM('Default', name='solarpanelmaterial'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['EnergyIns.id'], name='SolarPanels_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='SolarPanels_pkey')
    )
    # ### end Alembic commands ###