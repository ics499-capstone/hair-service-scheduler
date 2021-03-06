"""empty message

Revision ID: bcdd1151276f
Revises: 9a3cabec878b
Create Date: 2020-08-15 04:06:54.014061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcdd1151276f'
down_revision = '9a3cabec878b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.Column('price', flaskr.models.SqliteNumeric(length=5, collation=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    # ### end Alembic commands ###
