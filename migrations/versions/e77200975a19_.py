"""empty message

Revision ID: e77200975a19
Revises: 
Create Date: 2022-08-01 17:45:11.697231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e77200975a19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.String(length=900), nullable=True),
    sa.Column('correct_answer', sa.String(length=100), nullable=True),
    sa.Column('incorrect_answer_one', sa.String(length=100), nullable=True),
    sa.Column('incorrect_answer_two', sa.String(length=100), nullable=True),
    sa.Column('incorrect_answer_three', sa.String(length=100), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('question_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('highest_score', sa.Integer(), nullable=True),
    sa.Column('highest_category', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('match',
    sa.Column('match_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('lives', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('match_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('match')
    op.drop_table('user')
    op.drop_table('question')
    # ### end Alembic commands ###
