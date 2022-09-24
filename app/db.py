from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
DB_PATH = "postgres+psycopg2://db-url"
ECHO_LOG = False
engine = create_engine(DB_PATH, echo=ECHO_LOG)

Session = sessionmaker(bind=engine)
session = Session()
