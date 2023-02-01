from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, date
from ..models import matter_models, formule_models, history_models, identifier_models, user_models
from .. models.history import History

def create_history(db: Session, date: date, id_matter: int, id_identifier: int, value: int):
    history_db = history_models.History(date=date, id_matter=id_matter, id_identifier=id_identifier, value=value)
    db.add(history_db)
    db.commit()
    db.refresh(history_db)
    return history_db

def get_history(db: Session, date: date, id_identifier: int):
    return db.query(history_models.History).filter(history_models.History.date == date, history_models.History.id_identifier == id_identifier).first()

def update_history(db: Session, date: date, id_identifier: int, value: int):
    history_db = db.query(history_models.History).filter(history_models.History.date == date, history_models.History.id_identifier == id_identifier).first()
    history_db.value = value
    db.commit()
    return history_db

def delete_history(db: Session, date: date, id_identifier: int):
    history_db = db.query(history_models.History).filter(history_models.History.date == date, history_models.History.id_identifier == id_identifier).first()
    db.delete(history_db)
    db.commit()
