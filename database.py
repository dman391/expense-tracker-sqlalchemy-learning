import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine
env_path = find_dotenv()
load_dotenv(env_path)

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
    echo=True
)


Base = declarative_base()