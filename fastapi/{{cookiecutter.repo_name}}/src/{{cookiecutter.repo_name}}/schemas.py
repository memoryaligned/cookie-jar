from pydantic import BaseModel


class FirstDomainObject(BaseModel):
    id: int
    first: str
    created_at: str
    updated_at: str

    class Config:
        # allows the app to translate ORM objects automatically instead of
        # creating a dictionary and then loading into Pyndantic
        orm_mode = True
