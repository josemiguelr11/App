from models.formule import FormulaBase
from controllers.formule_crud import create_formule, update_formule, get_formule, delete_formule
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from sqlalchemy.orm import Session



app_formule = APIRouter()
@app_formule.post("/formulas/", response_model=FormulaBase)
def create_new_formule(formule:FormulaBase, db: Session = Depends(get_db)):
    db_formule = create_formule(db, formule)
    if db_formule:
        return db_formule
    raise HTTPException(status_code=400, detail="Formule already registered")

@app_formule.get("/formulas/", response_model=List[FormulaBase])
def read_formules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    formulas = get_formule(db, skip=skip, limit=limit)
    return formulas

@app_formule.put("/formulas/{primary_id}&{secondary_id}", response_model=FormulaBase)
def update_formulas(primary_id: int, secondary_id: int , db: Session = Depends(get_db)):
    db_formule = get_formule(db, primary_id=primary_id, secondary_id=secondary_id)
    if db_formule is None:
        raise HTTPException(status_code=404, detail="Formule not found")
    update_formule(db, db_formule, formule)
    return db_formule

@app_formule.delete("/formulas/{formule_id}", response_model=FormulaBase)
def delete_formulas(formule_id: int, db: Session = Depends(get_db)):
    db_formule = get_formule(db, formule_id=formule_id)
    if db_formule is None:
        raise HTTPException(status_code=404, detail="Formule not found")
    delete_formule(db, db_formule)
    return db_formule