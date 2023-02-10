from pydantic import BaseModel

class UserBase(BaseModel):
    user: str


class UserCreate(UserBase):
    password: str


class User(UserCreate):
    id: int
    class Config:
        orm_mode = True