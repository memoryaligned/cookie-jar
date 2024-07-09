import logging
import os

logger = logging.getLogger(__name__)


def get_db_connection_url() -> str:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        logging.info(
            "No .env file support; falling back to environment variables."
        )

    db_url: str = os.getenv("SQLALCHEMY_DATABASE_URL", "")

    if db_url == "" or "<USER>" in db_url or "<DBNAME>" in db_url:
        logging.critical(
            "SQLALCHEMY_DATABASE_URL environment variable is either not set "
            "or is missing the required <USER> and <DBNAME> information."
        )

    return db_url
