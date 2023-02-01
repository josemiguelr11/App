from sqlalchemy.orm import Session
from ..models import matter_models, formule_models, history_models, identifier_models, user_models
from .. models.matter import Matter
def create_matter(db: Session, matter:Matter):
    matter_db = Matter(id=matter.id, name=matter.name, user_id=matter.user_id)
    db.add(matter_db)
    db.commit()
    db.refresh(matter_db)
    return matter_db

def get_matter(db: Session, matter_id: int):
    return db.query(matter_models.Matter).filter(matter_models.Matter.id == matter_id).first()

def update_matter(db: Session, matter_id: int, name: str, user_id: int):
    matter_db = db.query(matter_models.Matter).filter(matter_models.Matter.id == matter_id).first()
    matter_db.name = name
    matter_db.user_id = user_id
    db.commit()
    return matter_db

def delete_matter(db: Session, matter_id: int):
    matter_db = db.query(matter_models.Matter).filter(matter_models.Matter.id == matter_id).first()
    db.delete(matter_db)
    db.commit()
