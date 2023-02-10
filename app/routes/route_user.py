from typing import List
from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from controllers.user_crud import create_user,  get_user, get_user_by_id, update_user, delete_user
from models.user import UserCreate, User
from sqlalchemy.orm import Session

app_user = APIRouter()


@app_user.post("/users/", response_model=User)
def create_new_user(user:UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    if db_user:
        return db_user
    raise HTTPException(status_code=400, detail="Email already registered")


@app_user.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_user(db, skip=skip, limit=limit)
    return users


@app_user.put("/users/{user_id}", response_model=User)
def update_users(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_user(db, db_user, user)
    return db_user

@app_user.delete("/users/{user_id}", response_model=User)
def delete_users(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, db_user)
    return db_user

