from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.types import Date
from {{cookiecutter.repo_name}}.database import Base
from {{cookiecutter.repo_name}}.database import engine


class FirstDomainObject(Base):
    __tablename__ = "first_domain_object"

    id = Column(Integer, primary_key=True, index=True)
    first = Column(String(256))
    created_at = Column(Date)
    updated_at = Column(Date)


def init_db():
    # create all tables
    Base.metadata.create_all(engine)
    return 0
