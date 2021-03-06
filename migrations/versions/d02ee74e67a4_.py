"""empty message

Revision ID: d02ee74e67a4
Revises: 3b58e68abc55
Create Date: 2022-05-11 16:17:56.361646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd02ee74e67a4'
down_revision = '3b58e68abc55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'users', ['user_id'], ['id'])
    op.add_column('pitch', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitch', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitch', type_='foreignkey')
    op.drop_column('pitch', 'user_id')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'user_id')
    # ### end Alembic commands ###
