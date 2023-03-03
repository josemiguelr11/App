from pydantic import BaseModel
#from typing import Union
#from matter import Matter

class Identifier(BaseModel):
    id_identifier: int
    name : str