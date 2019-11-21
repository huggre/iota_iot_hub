"""empty message

Revision ID: 89e05229fe58
Revises: 67bae6c9d0a4
Create Date: 2019-11-21 11:56:40.261732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89e05229fe58'
down_revision = '67bae6c9d0a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tbl_members_email', table_name='tbl_members')
    op.create_index(op.f('ix_tbl_members_email'), 'tbl_members', ['email'], unique=False)
    op.drop_index('ix_tbl_members_phone', table_name='tbl_members')
    op.create_index(op.f('ix_tbl_members_phone'), 'tbl_members', ['phone'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tbl_members_phone'), table_name='tbl_members')
    op.create_index('ix_tbl_members_phone', 'tbl_members', ['phone'], unique=1)
    op.drop_index(op.f('ix_tbl_members_email'), table_name='tbl_members')
    op.create_index('ix_tbl_members_email', 'tbl_members', ['email'], unique=1)
    # ### end Alembic commands ###
