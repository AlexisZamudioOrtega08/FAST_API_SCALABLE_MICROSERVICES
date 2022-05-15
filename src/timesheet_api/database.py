from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_env():
    load_dotenv(os.path.join('.env'))

    while os.getenv('MYSQL_USER') is None:
        load_dotenv(os.path.join(BASE_DIR, '.env'))
    username = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST")
    port = os.getenv("MYSQL_PORT")
    database = os.getenv("MYSQL_DB")
    return username, password, host, port, database

username, password, host, port, db = load_env()

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}".format(
    username=username,
    password=password,
    host=host,
    port=port,
    db_name=db
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()

