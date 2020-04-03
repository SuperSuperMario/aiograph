from sqlalchemy import create_engine, MetaData

from apps.settings import config
from apps.db import question, choice

DSN = 'mysql://{user}:{password}@{host}:{port}/{db}'


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])


if __name__ == '__main__':
    db_url = DSN.format(**config['mysql'])
    engine = create_engine(db_url)
    create_tables(engine)
