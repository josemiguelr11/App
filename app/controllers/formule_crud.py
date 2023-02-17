from sqlalchemy.orm import Session
from models.formule import FormulaBase
from models.formule_models import Formule


def create_formule(db: Session, formule:FormulaBase):
    formule = Formule(id_primary=formule.id_primary, id_secondary=formule.id_secondary, required=formule.required)
    db.add(formule)
    db.commit()
    db.refresh(formule)
    return formule

def get_formule(db: Session, skip:int, limit:int):
    return db.query(Formule).offset(skip).limit(limit).all()

def get_formule_by_id(db: Session, primary_id: int):
    return db.query(Formule).filter(Formule.id_primary == primary_id).all()

def get_formule_by_secondary(db: Session, primary_id: int, secondary_id: int):
    return db.query(Formule).filter(
        Formule.id_primary == primary_id, 
        Formule.id_secondary == secondary_id ).first()

def update_formule(db: Session, formule:Formule, required: float):
    formule.required = required
    db.commit()
    return formule

def delete_formule(db: Session, formule:Formule):
    db.delete(formule)
    db.commit()
