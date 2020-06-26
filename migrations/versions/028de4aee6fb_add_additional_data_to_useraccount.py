"""Add additional data to UserAccount

Revision ID: 028de4aee6fb
Revises: d6124c636bfe
Create Date: 2020-06-25 22:54:03.422469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '028de4aee6fb'
down_revision = 'd6124c636bfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('useraccount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('type', sa.Enum('customer', 'employee', 'admin', name='useraccounttype'), nullable=False),
    sa.Column('register_date', sa.DateTime(), nullable=False),
    sa.Column('register_confirmed', sa.Boolean(), nullable=False),
    sa.Column('register_complete', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_useraccount_email'), 'useraccount', ['email'], unique=True)
    op.create_index(op.f('ix_useraccount_username'), 'useraccount', ['username'], unique=True)
    op.drop_index('ix_user_account_email', table_name='user_account')
    op.drop_index('ix_user_account_username', table_name='user_account')
    op.drop_table('user_account')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_account',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_account_username', 'user_account', ['username'], unique=1)
    op.create_index('ix_user_account_email', 'user_account', ['email'], unique=1)
    op.drop_index(op.f('ix_useraccount_username'), table_name='useraccount')
    op.drop_index(op.f('ix_useraccount_email'), table_name='useraccount')
    op.drop_table('useraccount')
    # ### end Alembic commands ###
