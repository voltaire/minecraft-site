from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('mcuser', String(length=16)),
    Column('mcemail', String(length=120)),
    Column('applicant_age', SmallInteger, default=ColumnDefault(15)),
    Column('applicant_skills', String),
    Column('applicant_ip', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['applicant_ip'].create()
    post_meta.tables['user'].columns['applicant_skills'].create()
    post_meta.tables['user'].columns['mcemail'].create()
    post_meta.tables['user'].columns['mcuser'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['applicant_ip'].drop()
    post_meta.tables['user'].columns['applicant_skills'].drop()
    post_meta.tables['user'].columns['mcemail'].drop()
    post_meta.tables['user'].columns['mcuser'].drop()
