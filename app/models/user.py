from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    id: int
    user: str
    password:str