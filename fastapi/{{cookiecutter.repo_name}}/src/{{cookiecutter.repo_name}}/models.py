from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from {{cookiecutter.repo_name}}.database import Base, engine


def db_init() -> None:
    """Initialize the database with domain objects

    Args:
        None

    Returns:
        None
    """
    # create all tables
    Base.metadata.create_all(engine)
    return None


class FirstDomainObject(Base):
    __tablename__ = "first_domain_object"

    id = Column(Integer, primary_key=True, index=True)
    first = Column(String(256))
    created_at = Column(Date)
    updated_at = Column(Date)
