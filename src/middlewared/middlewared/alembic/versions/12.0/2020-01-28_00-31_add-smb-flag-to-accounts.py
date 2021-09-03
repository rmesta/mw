"""Add SMB flag to users and groups

Revision ID: 4abbf75347b2
Revises: f6a18dec20fa
Create Date: 2020-01-28 00:31:27.730182+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4abbf75347b2'
down_revision = 'f6a18dec20fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account_bsdgroups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bsdgrp_smb', sa.Boolean(), nullable=True))

    with op.batch_alter_table('account_bsdusers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bsdusr_smb', sa.Boolean(), nullable=True))

    op.execute("UPDATE account_bsdgroups SET bsdgrp_smb = 1 WHERE bsdgrp_builtin = 0")    
    op.execute("UPDATE account_bsdusers SET bsdusr_smb = 1 WHERE bsdusr_builtin = 0")    
    op.execute("UPDATE account_bsdgroups SET bsdgrp_smb = 0 WHERE bsdgrp_builtin = 1")    
    op.execute("UPDATE account_bsdusers SET bsdusr_smb = 0 WHERE bsdusr_builtin = 1")    

    with op.batch_alter_table('account_bsdgroups', schema=None) as batch_op:
        batch_op.alter_column('bsdgrp_smb', nullable=False)

    with op.batch_alter_table('account_bsdusers', schema=None) as batch_op:
        batch_op.alter_column('bsdusr_smb', nullable=False)

    # ### end Alembic commands ###
