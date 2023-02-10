from sqlalchemy.orm import Session
from models.matter_models import Matter
from models.matter import MatterCreate

def create_matter(db: Session, matter:MatterCreate):
    matter_db = Matter(name=matter.name, user_id=matter.user_id)
    db.add(matter_db)
    db.commit()
    db.refresh(matter_db)
    return matter_db

def get_matter(db: Session, skip:int, limit:int):
    return db.query(Matter).offset(skip).limit(limit).all()

def update_matter(db: Session, matter_id: int, name: str):
    matter_db = db.query(Matter).filter(Matter.id == matter_id).first()
    matter_db.name = name
    db.commit()
    return matter_db

def delete_matter(db: Session, matter_id: int):
    matter_db = db.query(Matter).filter(Matter.id == matter_id).first()
    db.delete(matter_db)
    db.commit()
