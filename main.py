from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from app.routes.route_user import app_user as route_user

# from  import crud, models, schemas
# from .database import SessionLocal, engine
from app.test.database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(route_user)
# Dependency



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=4000, reload=True)

