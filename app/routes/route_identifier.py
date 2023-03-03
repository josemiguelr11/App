from typing import List
from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from controllers.identifier_crud import create_identifier, get_identifier, update_identifier, delete_identifier
from models.identifier import Identifier
from sqlalchemy.orm import Session

app_identifier = APIRouter()

@app_identifier.post("/identifiers/", response_model=Identifier, tags=['Identificador'])
def create_new_identifier(identifier: Identifier, db: Session = Depends(get_db)):
    db_identifier = create_identifier(db, identifier)
    return db_identifier

@app_identifier.get("/identifiers/", response_model=List[Identifier], tags=['Identificador'])
def read_identifiers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    identifiers = get_identifier(db, skip=skip, limit=limit)
    return identifiers

@app_identifier.put("/identifiers/{identifier_id}", response_model=Identifier, tags=['Identificador'])
def update_identifiers(identifier_id: int, name: str, db: Session = Depends(get_db)):
    db_identifier = get_identifier(db, id_identifier=identifier_id)
    if db_identifier is None:
        raise HTTPException(status_code=404, detail="Identifier not found")
    db_identifier = update_identifier(db, identifier_id, name)
    return db_identifier

@app_identifier.delete("/identifiers/{identifier_id}", response_model=Identifier, tags=['Identificador'])
def delete_identifiers(identifier_id: int, db: Session = Depends(get_db)):
    db_identifier = get_identifier(db, id_identifier=identifier_id)
    if db_identifier is None:
        raise HTTPException(status_code=404, detail="Identifier not found")
    delete_identifier(db, identifier_id)
    return db_identifier
