from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
import jwt
from config.database import get_db
from controllers.user_crud import create_user,  get_user, get_user_by_id, update_user, delete_user, authenticate_user,get_user_by_name
from models.user import UserCreate, User
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jwt import encode

app_user = APIRouter()


@app_user.post("/users/", response_model=User, tags=['Usuario'])
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo usuario en la base de datos.

    Args:
        user (UserCreate): Los detalles del usuario que se van a crear.
        db (Session): La sesión de la base de datos a utilizar.

    Returns:
        User: El usuario recién creado.

    Raises:
        HTTPException: Si el email ya está registrado.
    """
    db_user = create_user(db, user)
    if db_user:
        return db_user
    raise HTTPException(status_code=400, detail="Email already registered")


@app_user.get("/users/", response_model=List[User], tags=['Usuario'])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista de todos los usuarios en la base de datos.

    Args:
        skip (int): La cantidad de usuarios para saltar en la lista.
        limit (int): La cantidad máxima de usuarios a devolver.
        db (Session): La sesión de la base de datos a utilizar.

    Returns:
        List[User]: Una lista de objetos User.
    """
    users = get_user(db, skip=skip, limit=limit)
    return users


@app_user.put("/users/{user_id}", response_model=User, tags=['Usuario'])
def update_users(user_id: int, password: str, db: Session = Depends(get_db)):
    """
    Actualiza la contraseña de un usuario existente en la base de datos.

    Args:
        user_id (int): El ID del usuario a actualizar.
        password (str): La nueva contraseña para el usuario.
        db (Session): La sesión de la base de datos a utilizar.

    Returns:
        User: El usuario actualizado.

    Raises:
        HTTPException: Si el usuario no se encuentra en la base de datos.
    """
    db_user = get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_user(db, db_user, password)
    return db_user

@app_user.delete("/users/{user_id}", response_model=User, tags=['Usuario'])
def delete_users(user_id: int, db: Session = Depends(get_db)):
    """
    Elimina un usuario existente de la base de datos.

    Args:
        user_id (int): El ID del usuario a eliminar.
        db (Session): La sesión de la base de datos a utilizar.

    Returns:
        User: El usuario eliminado.

    Raises:
        HTTPException: Si el usuario no se encuentra en la base de datos.
    """
    db_user = get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, db_user)
    return db_user


SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@app_user.post("/token", tags=['Auth'])
async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Autentica un usuario y genera un token de acceso.

    Args:
        db (Session): La sesión de la base de datos a utilizar.
        form_data (OAuth2PasswordRequestForm): Los datos del formulario de inicio de sesión.

    Returns:
        dict: Un diccionario que contiene el token de acceso y su tipo.

    Raises:
        HTTPException: Si las credenciales de inicio de sesión son inválidas.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_payload = {
        "sub": user.user,
        "exp": datetime.utcnow() + access_token_expires
    }
    access_token = encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}


@app_user.get("/users/token", tags=['Auth'])
async def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """
    Obtiene la información del usuario que realizó la solicitud.

    Args:
        db (Session): La sesión de la base de datos a utilizar.
        token (str): El token de acceso proporcionado por el usuario.

    Returns:
        User: El usuario que realizó la solicitud.

    Raises:
        HTTPException: Si las credenciales de inicio de sesión son inválidas o si el usuario no se encuentra en la base de datos.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_name: str = payload.get("sub")
        if user_name is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = get_user_by_name(db, user_name)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
