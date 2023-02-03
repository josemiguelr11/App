from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .app.models import user_models,formule_models, schemas, matter_models, history_models,identifier_models
from .app.controllers import user_crud,history_crud,formule_crud,identifier_crud,matter_crud
from .app.test.database import SessionLocal, engine

user_models,formule_models, matter_models, history_models,identifier_models.create_all(bind=engine)
import uvicorn
from app.routes.route_user import app_user as route_user

# from  import crud, models, schemas
# from .database import SessionLocal, engine
from app.test.database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(route_user)
# Dependency


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=4000, reload=True)

