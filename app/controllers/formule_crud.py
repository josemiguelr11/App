from sqlalchemy.orm import Session
from models.formule import FormulaBase
from models.formule_models import Formule


def create_formule(db: Session, formule:FormulaBase):
    formule = Formule(id_primary=formule.id_primary, id_secondary=formule.id_secondary, required=formule.required)
    db.add(formule)
    db.commit()
    db.refresh(formule)
    return formule

def get_formule(db: Session):
    return db.query(Formule).all()

def get_formule_by_id(db: Session, primary_id: int):
    return db.query(Formule).filter(Formule.id_primary == primary_id).first()

def get_formule_by_id(db: Session, primary_id: int, secondary_id: int):
    return db.query(Formule).filter(
        Formule.primary_id == primary_id, 
        Formule.secondary_id == secondary_id ).first()

def update_formule(db: Session, id_primary: int, id_secondary: int, required: float):
    formule = db.query(Formule).filter(
        Formule.id_primary == id_primary,
        Formule.id_secondary == id_secondary
        ).first()
    formule.required = required
    db.commit()
    return formule

def delete_formule(db: Session, id_primary: int):
    formule = db.query(Formule).filter(Formule.id_primary == id_primary).all()
    db.delete(formule)
    db.commit()

def delete_formule(db: Session, id_primary: int, id_secundary: int):
    formule = db.query(Formule).filter(
        Formule.id_primary == id_primary,
        Formule.id_secundary == id_secundary
        ).first()
    db.delete(formule)
    db.commit()
