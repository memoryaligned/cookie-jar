import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from {{cookiecutter.repo_name}}.models import UserModel
from {{cookiecutter.repo_name}}.services.database import Base


@pytest_asyncio.fixture(scope="session")
async def session():
    db_url: str = "sqlite+aiosqlite:///:memory:"
    engine = create_async_engine(db_url)
    session = AsyncSession(engine)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield session
        await session.close()


@pytest.mark.asyncio
async def test_user_model(session):
    await UserModel.create(session, id="1", email="john@gmail.com", full_name="John Doe")
    actual = await UserModel.get(session, id="1")
    assert isinstance(actual, UserModel)
