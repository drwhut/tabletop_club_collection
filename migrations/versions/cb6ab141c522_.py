"""empty message

Revision ID: cb6ab141c522
Revises: 7a48dbd05780
Create Date: 2020-07-08 21:03:51.856561

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from app.models import Package


# revision identifiers, used by Alembic.
revision = 'cb6ab141c522'
down_revision = '7a48dbd05780'
branch_labels = None
depends_on = None


def upgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.create_table('maintainers',
	sa.Column('user_id', sa.Integer(), nullable=False),
	sa.Column('package_id', sa.Integer(), nullable=False),
	sa.ForeignKeyConstraint(['package_id'], ['package.id'], ),
	sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
	sa.PrimaryKeyConstraint('user_id', 'package_id')
	)

	bind = op.get_bind()
	session = orm.Session(bind=bind)

	op.execute('INSERT INTO maintainers (package_id, user_id) SELECT id, author_id FROM package;')

	session.commit()

	# ### end Alembic commands ###


def downgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.drop_table('maintainers')
	# ### end Alembic commands ###
