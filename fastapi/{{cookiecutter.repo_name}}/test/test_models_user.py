import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from {{cookiecutter.repo_name}}.models import UserModel
from {{cookiecutter.repo_name}}.services.database import Base


@pytest.mark.asyncio
async def test_user_model():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    session = AsyncSession(engine)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await UserModel.create(session, id="1", email="john@gmail.com", full_name="Jone Doe")
    actual = await UserModel.get(session, id="1")
    assert isinstance(actual, UserModel)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
