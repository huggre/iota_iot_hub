"""empty message

Revision ID: dccf443b075c
Revises: 
Create Date: 2021-03-31 00:07:44.614580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dccf443b075c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('remaining_time', sa.Integer(), nullable=True),
    sa.Column('payment_address', sa.String(length=64), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.Column('modified_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['tbl_members.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['tbl_members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tbl_devices_created_on'), 'tbl_devices', ['created_on'], unique=False)
    op.create_index(op.f('ix_tbl_devices_modified_on'), 'tbl_devices', ['modified_on'], unique=False)
    op.drop_index('ix_tbl_services_created_on', table_name='tbl_services')
    op.drop_index('ix_tbl_services_modified_on', table_name='tbl_services')
    op.drop_table('tbl_services')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_services',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(length=64), nullable=True),
    sa.Column('status', sa.BOOLEAN(), nullable=True),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('remaining_time', sa.INTEGER(), nullable=True),
    sa.Column('payment_address', sa.TEXT(length=64), nullable=True),
    sa.Column('created_on', sa.DATETIME(), nullable=True),
    sa.Column('created_by', sa.INTEGER(), nullable=True),
    sa.Column('modified_on', sa.DATETIME(), nullable=True),
    sa.Column('modified_by', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['tbl_members.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['tbl_members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tbl_services_modified_on', 'tbl_services', ['modified_on'], unique=False)
    op.create_index('ix_tbl_services_created_on', 'tbl_services', ['created_on'], unique=False)
    op.drop_index(op.f('ix_tbl_devices_modified_on'), table_name='tbl_devices')
    op.drop_index(op.f('ix_tbl_devices_created_on'), table_name='tbl_devices')
    op.drop_table('tbl_devices')
    # ### end Alembic commands ###