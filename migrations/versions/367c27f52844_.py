"""empty message

Revision ID: 367c27f52844
Revises: 547984158f20
Create Date: 2020-08-15 04:11:43.730998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '367c27f52844'
down_revision = '547984158f20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service', sa.Column('price', flaskr.models.SqliteNumeric(length=5, collation=2), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service', 'price')
    # ### end Alembic commands ###
