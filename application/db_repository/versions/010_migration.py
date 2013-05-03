from sqlalchemy.dialects import postgresql
from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
minecraft_servers = Table('minecraft_servers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('server_name', String(length=140)),
    Column('server_address', postgresql.INET),
    Column('server_port', SmallInteger),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['minecraft_servers'].columns['server_address'].create()
    post_meta.tables['minecraft_servers'].columns['server_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['minecraft_servers'].columns['server_address'].drop()
    post_meta.tables['minecraft_servers'].columns['server_name'].drop()
