from pydantic import BaseModel
from typing import Union
from .matter import Matter

class FormulaBase(BaseModel):
    id_primary: Matter
    id_secondary: Matter
    required: float
    