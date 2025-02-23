"""Adicionando tabela Rota

Revision ID: 0efc737d9a35
Revises: 1af236e8559e
Create Date: 2025-02-05 18:44:52.379218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0efc737d9a35'
down_revision = '1af236e8559e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rota',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rota')
    # ### end Alembic commands ###
