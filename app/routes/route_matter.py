from typing import List
from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from controllers.matter_crud import create_matter, get_matter
from models.matter import Matter, MatterCreate
from sqlalchemy.orm import Session

app_matter = APIRouter()

@app_matter.post("/matter/", response_model=Matter)
def create_new_matter(matter:MatterCreate, db: Session = Depends(get_db)):
    db_matter = create_matter(db, matter)
    if db_matter:
        return db_matter
    raise HTTPException(status_code=400, detail="Email already registered")


@app_matter.get("/matter/", response_model=List[Matter])
def read_matters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matters = get_matter(db, skip=skip, limit=limit)
    return matters


# @app.get("/matters/{matter_id}", response_model=schemas.matter)
# def read_matter(matter_id: int, db: Session = Depends(get_db)):
#     db_matter = crud.get_matter(db, matter_id=matter_id)
#     if db_matter is None:
#         raise HTTPException(status_code=404, detail="matter not found")
#     return db_matter


# @app.post("/matters/{matter_id}/items/", response_model=schemas.Item)
# def create_item_for_matter(
#     matter_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_matter_item(db=db, item=item, matter_id=matter_id)
