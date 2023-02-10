from pydantic import BaseModel
from typing import Union

class MatterCreate(BaseModel):
    name: str
    user_id: int

class Matter(MatterCreate):
    id: int
    class Config:
        orm_mode = True