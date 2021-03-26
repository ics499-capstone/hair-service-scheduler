"""Service and Appointment table

Revision ID: 830aea8785c5
Revises: bb11aa27666a
Create Date: 2020-08-15 04:00:12.604901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '830aea8785c5'
down_revision = 'bb11aa27666a'
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
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['useraccount.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointment')
    op.drop_table('service')
    # ### end Alembic commands ###