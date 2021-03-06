"""Unique iscsi_target_extent_name

Revision ID: 2e2c8b0e787b
Revises: 50c8360d9616
Create Date: 2021-05-10 13:44:29.872200+00:00

"""
import itertools

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e2c8b0e787b'
down_revision = '50c8360d9616'
branch_labels = None
depends_on = None


def ensure_unique_string(conn, table, column):
    values = set()
    for row in conn.execute(f"SELECT * FROM {table}").fetchall():
        value = row[column]
        if value is not None:
            update = False
            if value in values:
                update = True
                for i in itertools.count(1):
                    new_value = value + str(i)
                    if new_value not in values:
                        value = new_value
                        break

            if update:
                conn.execute(f"UPDATE {table} SET {column} = ? WHERE id = ?", [value, row["id"]])

            values.add(value)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()

    ensure_unique_string(conn, 'services_iscsitargetextent', 'iscsi_target_extent_name')
    with op.batch_alter_table('services_iscsitargetextent', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_services_iscsitargetextent_iscsi_target_extent_name'), ['iscsi_target_extent_name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services_iscsitargetextent', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_services_iscsitargetextent_iscsi_target_extent_name'), type_='unique')

    # ### end Alembic commands ###
