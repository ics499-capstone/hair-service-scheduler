"""empty message

Revision ID: 547984158f20
Revises: 54bb0c450536
Create Date: 2020-08-15 04:10:21.050814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '547984158f20'
down_revision = '54bb0c450536'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service', sa.Column('description', sa.String(length=512), nullable=True))
    op.add_column('service', sa.Column('price', flaskr.models.SqliteNumeric(length=5, collation=2), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service', 'price')
    op.drop_column('service', 'description')
    # ### end Alembic commands ###
