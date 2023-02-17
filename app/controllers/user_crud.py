from sqlalchemy.orm import Session

from models.user import UserCreate
from models.user_models import User
from models import user_models

def create_user(db: Session, user:UserCreate):
    user_db = User(user=user.user, password=user.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def get_user(db: Session, skip:int, limit:int):
    return db.query(user_models.User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()

def update_user(db: Session, user_old:User, password:str):
    user_old.password = password
    db.commit()
    return user_old

def delete_user(db: Session, user_db: user_models.User):
    db.delete(user_db)
    db.commit()


