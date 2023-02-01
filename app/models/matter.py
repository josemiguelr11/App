from pydantic import BaseModel
from typing import Union

class Matter(BaseModel):
    id: int
    name: str
    user_id: int
