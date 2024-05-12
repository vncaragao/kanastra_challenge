"""empty message

Revision ID: 47505170c72e
Revises: 
Create Date: 2024-05-11 10:08:11.152596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47505170c72e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('file_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('governmentId', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('debtAmount', sa.Float(), nullable=False),
    sa.Column('debtDueDate', sa.Date(), nullable=False),
    sa.Column('debtId', sa.String(length=50), nullable=False),
    sa.Column('date_event', sa.DateTime(), nullable=False),
    sa.Column('processed', sa.SmallInteger(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['files.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file_items')
    op.drop_table('files')
    # ### end Alembic commands ###
