from pydantic import BaseModel
from typing import Union

class History(BaseModel):
    date: str
    id_matter: int
    id_identifier: int
    value: int