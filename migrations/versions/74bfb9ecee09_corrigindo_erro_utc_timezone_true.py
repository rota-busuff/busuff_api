"""Corrigindo erro UTC - timezone=True

Revision ID: 74bfb9ecee09
Revises: 1c397c71413f
Create Date: 2025-02-04 22:14:32.272763

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '74bfb9ecee09'
down_revision = '1c397c71413f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('historico', schema=None) as batch_op:
        batch_op.alter_column('data',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('historico', schema=None) as batch_op:
        batch_op.alter_column('data',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)

    # ### end Alembic commands ###
