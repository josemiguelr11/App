from pydantic import BaseModel
from .matter import Matter

class FormulaBase(BaseModel):
    id_primary: int
    id_secondary: int
    required: float
    class Config:
        orm_mode = True
    