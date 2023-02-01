from pydantic import BaseModel
from typing import Union
from matter import Matter

class Formula(BaseModel):
    id_primary: Matter
    id_secundary: Matter
    required: float