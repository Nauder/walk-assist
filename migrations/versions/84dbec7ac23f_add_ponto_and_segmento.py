"""add ponto and segmento

Revision ID: 84dbec7ac23f
Revises: 06a239c84f93
Create Date: 2023-11-16 13:16:58.400995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84dbec7ac23f'
down_revision = '06a239c84f93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('registro',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('registro',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
