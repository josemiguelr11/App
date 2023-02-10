from typing import List
from fastapi import APIRouter, Depends, HTTPException
from config.database import get_db
from controllers.user_crud import create_user,  get_user
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


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
