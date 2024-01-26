from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from {{cookiecutter.repo_name}}.models import UserModel
from {{cookiecutter.repo_name}}.services.database import get_db

router = APIRouter(prefix="/user", tags=["user"])


class UserSchemaBase(BaseModel):
    first: str | None = None


class UserSchemaCreate(UserSchemaBase):
    pass


class UserSchema(UserSchemaBase):
    id: str
    created_at: str
    updated_at: str

    class Config:
        orm_model = True


@router.get("/get-first", response_model=UserSchema)
async def get_first(id: str, db: AsyncSession = Depends(get_db)):
    user = await UserModel.get(db, id)
    return user


@router.get("/get-users", response_model=list[UserSchema])
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await UserModel.get_all(db)
    return users


@router.post("/create-user", response_model=UserSchema)
async def create_user(user: UserSchemaCreate, db: AsyncSession = Depends(get_db)):
    user await UserModel.create(db, **user.dict())
    return user
