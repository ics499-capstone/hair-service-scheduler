"""Add UserAccount table {id, username, email, password_hash, phone_number}

Revision ID: d6124c636bfe
Revises: 
Create Date: 2020-06-25 22:27:34.912104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6124c636bfe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_account_email'), 'user_account', ['email'], unique=True)
    op.create_index(op.f('ix_user_account_username'), 'user_account', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_account_username'), table_name='user_account')
    op.drop_index(op.f('ix_user_account_email'), table_name='user_account')
    op.drop_table('user_account')
    # ### end Alembic commands ###
