
from fastapi import FastAPI
import uvicorn
from routes.route_user import app_user as route_user
from routes.route_matter import app_matter as route_matter
from routes.route_formule import app_formule as route_formule
from fastapi.middleware.cors import CORSMiddleware
# from  import crud, models, schemas
# from .database import SessionLocal, engine
from config.database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(route_user)
app.include_router(route_matter)
app.include_router(route_formule)

# Dependency

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4000",
    "http://localhost:5000",
    "http://localhost:8000",
    "http://localhost:8080",
]

# Agregar el middleware de CORS a la aplicación de FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=4000, reload=True)

