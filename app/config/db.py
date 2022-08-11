from sqlite3 import threadsafety
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker



DATABASES= create_engine('sqlite:///kwg.db')
meta=MetaData()

Session = sessionmaker(DATABASES)
session = Session()

conn = DATABASES.connect()