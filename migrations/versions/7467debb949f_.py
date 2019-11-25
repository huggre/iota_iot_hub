"""empty message

Revision ID: 7467debb949f
Revises: d0a128c0e56d
Create Date: 2019-11-25 14:07:15.884707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7467debb949f'
down_revision = 'd0a128c0e56d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_assets', sa.Column('balance', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_assets', 'balance')
    # ### end Alembic commands ###
