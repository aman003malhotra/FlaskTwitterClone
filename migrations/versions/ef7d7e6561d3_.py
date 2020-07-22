"""empty message

Revision ID: ef7d7e6561d3
Revises: dfaaeefdb3ad
Create Date: 2020-01-15 16:13:58.989067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef7d7e6561d3'
down_revision = 'dfaaeefdb3ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follower',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followee_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follower')
    # ### end Alembic commands ###
