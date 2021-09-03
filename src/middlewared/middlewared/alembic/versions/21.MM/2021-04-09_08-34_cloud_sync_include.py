"""Cloud Sync Include

Revision ID: e6aa9844e0c4
Revises: 72fc294965d1
Create Date: 2021-04-09 08:34:19.183369+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6aa9844e0c4'
down_revision = '72fc294965d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks_cloudsync', schema=None) as batch_op:
        batch_op.add_column(sa.Column('include', sa.TEXT(), nullable=True))

    op.execute("UPDATE tasks_cloudsync SET include = '[]'")

    with op.batch_alter_table('tasks_cloudsync', schema=None) as batch_op:
        batch_op.alter_column('include', existing_type=sa.TEXT(), nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks_cloudsync', schema=None) as batch_op:
        batch_op.drop_column('include')

    # ### end Alembic commands ###
