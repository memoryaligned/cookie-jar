import logging
import os
import sys

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL", "")
if (
        SQLALCHEMY_DATABASE_URL == ""
        or "<USER>" in SQLALCHEMY_DATABASE_URL
        or "<DBNAME>" in SQLALCHEMY_DATABASE_URL
):
    logging.critical(
        "SQLALCHEMY_DATABASE_URL environment variable not set correctly "
        "in the .env file (or environment)"
    )
    sys.exit(1)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
