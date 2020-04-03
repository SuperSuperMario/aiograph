import aiomysql.sa

from sqlalchemy import (MetaData, Table, Column,
                        ForeignKey, Integer, String, Date)
from sqlalchemy.orm import relationship

meta = MetaData()

question = Table(
    'question', meta,
    Column('id', Integer, primary_key=True),
    Column('question_text', String(200), nullable=False),
    Column('pub_date', Date, nullable=False)
)


choice = Table(
    'choice', meta,
    Column('id', Integer, primary_key=True),
    Column('choice_text', String(100), nullable=False, comment='选择内容'),
    Column('votes', Integer, server_default='0', nullable=False),

    Column('question_id', Integer, ForeignKey(
        'question.id', ondelete='CASCADE'))

    
)


async def init_db(app):
    conf = app['config']['mysql']
    if conf.get('database'):
        conf['db'] = conf['database']
        del conf['database']
    engine = await aiomysql.sa.create_engine(**conf)
    app['db'] = engine
    app['logger'].warning('~~~~start db conn~~~~')


async def close_db(app):
    app['logger'].warning('~~~~clean db conn~~~~')
    app['db'].close()
    await app['db'].wait_closed()
