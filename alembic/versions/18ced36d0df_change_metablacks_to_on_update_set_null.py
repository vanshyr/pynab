"""change metablacks to on-update set-null

Revision ID: 18ced36d0df
Revises: 8ba8c933e2
Create Date: 2015-06-19 12:33:55.629954

"""

# revision identifiers, used by Alembic.
revision = '18ced36d0df'
down_revision = '8ba8c933e2'

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('releases_movie_metablack_id_fkey', 'releases')
    op.drop_constraint('releases_nfo_metablack_id_fkey', 'releases')
    op.drop_constraint('releases_tvshow_metablack_id_fkey', 'releases')
    op.drop_constraint('releases_rar_metablack_id_fkey', 'releases')
    op.drop_constraint('releases_sfv_metablack_id_fkey', 'releases')

    op.create_foreign_key('releases_movie_metablack_id_fkey', 'releases', 'metablack', ['movie_metablack_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('releases_nfo_metablack_id_fkey', 'releases', 'metablack', ['nfo_metablack_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('releases_rar_metablack_id_fkey', 'releases', 'metablack', ['rar_metablack_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('releases_sfv_metablack_id_fkey', 'releases', 'metablack', ['sfv_metablack_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('releases_tvshow_metablack_id_fkey', 'releases', 'metablack', ['tvshow_metablack_id'], ['id'], ondelete='SET NULL')
    
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
