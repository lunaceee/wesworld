# delete from cache
# where created_at < now() - interval '3 days';
import os
import datetime
import sqlalchemy
from sqlalchemy.schema import Table
from sqlalchemy.schema import MetaData

print 'Running cron job'


too_old = datetime.datetime.today() - datetime.timedelta(days=3)
db_url = os.environ.get('DATABASE_URL', 'postgresql:///wesworld')
engine = sqlalchemy.create_engine(db_url)
meta = MetaData()
meta.reflect(bind=engine)
cache_table = meta.tables['cache']
engine.execute(cache_table.delete().where(cache_table.c.created_at <= too_old))
