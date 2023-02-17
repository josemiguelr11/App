from typing import List
from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from controllers.history_crud import create_history, get_history, update_history, delete_history
from models.history import History
from sqlalchemy.orm import Session

app_history = APIRouter()

@app_history.post("/history/", response_model=History, tags=['Historia'])
def create_new_history(history: History, db: Session = Depends(get_db)):
    db_history = create_history(db, history)
    return db_history

@app_history.get("/history/", response_model=List[History], tags=['Historia'])
def read_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    histories = get_history(db, skip=skip, limit=limit)
    return histories

@app_history.put("/history/{history_id}", response_model=History, tags=['Historia'])
def update_history_item(history_id: int, description: str, db: Session = Depends(get_db)):
    db_history = get_history(db, history_id=history_id)
    if db_history is None:
        raise HTTPException(status_code=404, detail="History item not found")
    db_history = update_history(db, db_history, description)
    return db_history

@app_history.delete("/history/{history_id}", response_model=History, tags=['Historia'])
def delete_history_item(history_id: int, db: Session = Depends(get_db)):
    db_history = get_history(db, history_id=history_id)
    if db_history is None:
        raise HTTPException(status_code=404, detail="History item not found")
    delete_history(db, db_history)
    return db_history
