from sqlalchemy.orm import Session
from ..models import formule_models
from .. models.formule import Formule

def create_formule(db: Session, formule:Formule):
    formule = Formule(id_primary=formule.id_primary, id_secundary=formule.id_secundary, required=formule.required)
    db.add(formule)
    db.commit()
    db.refresh(formule)
    return formule

def get_formule(db: Session, id_primary: int):
    return db.query(formule_models.Formule).filter(formule_models.Formule.id_primary == id_primary).first()

def update_formule(db: Session, id_primary: int, id_secundary: int, required: float):
    formule = db.query(formule_models.Formule).filter(formule_models.Formule.id_primary == id_primary).first()
    formule.id_secundary = id_secundary
    formule.required = required
    db.commit()
    return formule

def delete_formule(db: Session, id_primary: int):
    formule = db.query(formule_models.Formule).filter(formule_models.Formule.id_primary == id_primary).first()
    db.delete(formule)
    db.commit()
