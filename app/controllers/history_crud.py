from sqlalchemy.orm import Session
from datetime import date
from models import history_models
from models.history import History

def create_history(db: Session, history:History):
    history_db = History(date=history.date, id_matter=history.id_matter, id_identifier=history.id_identifier, value=history.value)
    db.add(history_db)
    db.commit()
    db.refresh(history_db)
    return history_db

def get_history(db: Session, date: date, id_history: int):
    return db.query(history_models.History).filter(history_models.History.date == date, history_models.History.id_history == id_history).first()

def update_history(db: Session, date: date, id_history: int, value: int):
    history_db = db.query(history_models.History).filter(history_models.History.date == date, history_models.History.id_history == id_history).first()
    history_db.value = value
    db.commit()
    return history_db

def delete_history(db: Session, id_history: int):
    history_db = db.query(history_models.History).filter(history_models.History.id_history == id_history).first()
    if not history_db:
        return None
    db.delete(history_db)
    db.commit()
    return history_db