from sqlalchemy.orm import Session
from .. models.user import User
from ..models import user_models

def create_user(db: Session, user:User):
    user_db = User(user=user.user, password=user.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def get_user(db: Session):
    return db.query(user_models.User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()

def update_user(db: Session, user_id: int, user: str, password: str):
    user_db = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    user_db.user = user
    user_db.password = password
    db.commit()
    return user_db

def delete_user(db: Session, user_id: int):
    user_db = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    db.delete(user_db)
    db.commit()


