# delete from cache
# where created_at < now() - interval '3 days';
import datetime
import sqlalchemy
from sqlalchemy.schema import Table
from sqlalchemy.schema import MetaData

too_old = datetime.datetime.today() - datetime.timedelta(days=3)
engine = sqlalchemy.create_engine('postgresql:///wesworld')
meta = MetaData()
meta.reflect(bind=engine)
cache_table = meta.tables['cache']
engine.execute(cache_table.delete().where(cache_table.c.created_at <= too_old))