"""ad_place

Revision ID: da51784bba7c
Revises: 57ecda91505a
Create Date: 2022-01-29 00:37:28.527772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da51784bba7c'
down_revision = '57ecda91505a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ad_places',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('place_id', sa.String(), nullable=False),
    sa.Column('publisher', sa.Integer(), nullable=True),
    sa.Column('adspot_type', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adspot_type'], ['adspot_types.id'], ),
    sa.ForeignKeyConstraint(['publisher'], ['publishers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('adspots', sa.Column('ad_place_id', sa.Integer(), nullable=True))
    op.add_column('adspots', sa.Column('spot_metadata', sa.String(), nullable=True))
    op.drop_constraint('adspots_adspot_type_id_fkey', 'adspots', type_='foreignkey')
    op.drop_constraint('adspots_publisher_id_fkey', 'adspots', type_='foreignkey')
    op.create_foreign_key(None, 'adspots', 'ad_places', ['ad_place_id'], ['id'])
    op.drop_column('adspots', 'publisher_id')
    op.drop_column('adspots', 'adspot_type_id')
    op.drop_column('adspots', 'ad_metadata')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('adspots', sa.Column('ad_metadata', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('adspots', sa.Column('adspot_type_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('adspots', sa.Column('publisher_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'adspots', type_='foreignkey')
    op.create_foreign_key('adspots_publisher_id_fkey', 'adspots', 'publishers', ['publisher_id'], ['id'])
    op.create_foreign_key('adspots_adspot_type_id_fkey', 'adspots', 'adspot_types', ['adspot_type_id'], ['id'])
    op.drop_column('adspots', 'spot_metadata')
    op.drop_column('adspots', 'ad_place_id')
    op.drop_table('ad_places')
    # ### end Alembic commands ###
