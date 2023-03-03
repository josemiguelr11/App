from collections import defaultdict
from sqlalchemy.orm import Session
from models.matter_models import Matter
from querys.matter_querys import query_get_matter_and_submatter_by_user
from models.matter import MatterCreate
from sqlalchemy import text

def create_matter(db: Session, matter: MatterCreate):
    matter_db = Matter(name=matter.name, user_id=matter.user_id)
    db.add(matter_db)
    db.commit()
    db.refresh(matter_db)
    return matter_db

def get_matter(db: Session, skip: int, limit: int):
    return db.query(Matter).limit(limit).offset(skip).all()

def get_matter_by_id(db: Session, matter_id: int):
    return db.query(Matter).filter(Matter.id == matter_id).first()

def get_matter_by_user(db: Session, user_id: int):
    return db.query(Matter).filter(Matter.user_id == user_id).all()

def get_matter_by_user_id(db: Session, user_id: int):
    query = text(query_get_matter_and_submatter_by_user(user_id))
    matter_by_user = db.execute(query).mappings().all()
    # Agrupar por id de materia prima
    groups = defaultdict(list)
    for d in matter_by_user:
        id_mp = d['id']
        mp = d['name']
        qty = d['required']
        secondary_id = d['secondary_id']
        secondary_name = d['secondary_name']
        user_id = d['user_id']
        groups[id_mp].append((mp, qty, secondary_id, secondary_name, user_id))

    # Combinar elementos con el mismo id de materia prima
    result = []

    for id_mp, group in groups.items():
        mp = group[0][0]
        parts = [{
            'secondary_id': secondary_id,
            'secondary_name': secondary_name,
            'required': qty
            } for _, qty, secondary_id, secondary_name, _ in group]
        user_id = group[0][4]
        result.append({'id': id_mp, 'name': mp,
                       'secondary': parts, 'user_id': user_id})

    return result

def update_matter(db: Session, matter_db: Matter, name: str):
    matter_db.name = name
    db.commit()
    return matter_db

def delete_matter(db: Session, matter_db: Matter):
    db.delete(matter_db)
    db.commit()
