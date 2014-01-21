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
    Column('fishban_check', Boolean),
)

user_application = Table('user_application', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=140)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].create()
    post_meta.tables['user_application'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].drop()
    post_meta.tables['user_application'].drop()
