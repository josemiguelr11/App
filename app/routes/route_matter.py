from typing import List
from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from controllers.matter_crud import create_matter, get_matter, get_matter_by_id, update_matter, delete_matter
from models.matter import Matter, MatterCreate
from sqlalchemy.orm import Session

app_matter = APIRouter()

@app_matter.post("/matter/", response_model=Matter, tags=['Materiales'])
def create_new_matter(matter:MatterCreate, db: Session = Depends(get_db)):
    db_matter = create_matter(db, matter)
    if db_matter:
        return db_matter
    raise HTTPException(status_code=400, detail="Email already registered")

@app_matter.get("/matter/", response_model=List[Matter], tags=['Materiales'])
def read_matters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matters = get_matter(db=db, limit=limit, skip=skip)
    return matters
    
@app_matter.delete("/matter/{matter_id}", tags=['Materiales'])
def delete_matter_id(matter_id: int, db: Session = Depends(get_db)):
    matter = get_matter_by_id(db, matter_id)
    if matter:
        delete_matter(db, matter)
        return {"message": "Matter deleted successfully"}
    raise HTTPException(status_code=404, detail="Matter not found")

@app_matter.put("/matter/{matter_id}", tags=['Materiales'])
def update_matter_by_id(matter_id: int, matter_name: str, db: Session = Depends(get_db)):
    db_matter = get_matter_by_id(db, matter_id)
    if db_matter:
        update_matter(db, db_matter, matter_name)
        return {"message": "Matter updated successfully"}
    raise HTTPException(status_code=404, detail="Matter not found")

