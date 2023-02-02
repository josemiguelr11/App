from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date
from ..models import matter_models, formule_models, history_models, identifier_models, user_models
from .. models.identifier import Identifier

def create_identifier(db: Session, identifier: Identifier):
    identifier_db = Identifier(id_identifier=identifier.id_identifier, name=identifier.name)
    db.add(identifier_db)
    db.commit()
    db.refresh(identifier_db)
    return identifier_db

def get_identifier(db: Session, id_identifier: int):
    return db.query(identifier_models.Identifier).filter(identifier_models.Identifier.id_identifier == id_identifier).first()

def update_identifier(db: Session, id_identifier: int, name: str):
    identifier_db = db.query(identifier_models.Identifier).filter(identifier_models.Identifier.id_identifier == id_identifier).first()
    identifier_db.name = name
    db.commit()
    return identifier_db

def delete_identifier(db: Session, id_identifier: int):
    identifier_db = db.query(identifier_models.Identifier).filter(identifier_models.Identifier.id_identifier == id_identifier).first()
    db.delete(identifier_db)
    db.commit()
