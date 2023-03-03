from sqlalchemy.orm import Session
from models.user import UserCreate
from models.user_models import User
from models import user_models
from passlib.context import CryptContext
from typing import List, Union

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica que la contraseña en texto plano coincida con la contraseña hasheada.

    Parameters:
        plain_password (str): La contraseña en texto plano a verificar.
        hashed_password (str): La contraseña hasheada contra la que se verificará.

    Returns:
        bool: True si las contraseñas coinciden, False en caso contrario.

    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Obtiene la versión hasheada de una contraseña en texto plano.

    Parameters:
        password (str): La contraseña en texto plano a hashear.

    Returns:
        str: La versión hasheada de la contraseña.

    """
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str) -> Union[User, bool]:
    """
    Autentica a un usuario en la base de datos.

    Parameters:
        db (Session): Una sesión de base de datos.
        email (str): El correo electrónico del usuario.
        password (str): La contraseña del usuario.

    Returns:
        User | bool: Si la autenticación es exitosa, retorna el objeto User correspondiente al usuario autenticado. Si la autenticación falla, retorna False.

    """
    user = db.query(User).filter(User.user == email).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_user(db: Session, user: UserCreate) -> User:
    """
    Crea un nuevo usuario en la base de datos.

    Parameters:
        db (Session): Una sesión de base de datos.
        user (UserCreate): El objeto UserCreate con los datos del nuevo usuario.

    Returns:
        User: El objeto User correspondiente al usuario creado.

    """
    hashed_password = pwd_context.hash(user.password)
    user_db = User(user=user.user, password=hashed_password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


def get_user(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """
    Obtiene una lista de usuarios de la base de datos.

    Parameters:
        db (Session): Una sesión de base de datos.
        skip (int): El número de usuarios a saltar al principio de la lista.
        limit (int): El número máximo de usuarios a devolver.

    Returns:
        List[User]: Una lista de objetos User.

    """
    return db.query(user_models.User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int) -> User:
    """
    Obtiene un usuario de la base de datos por su ID.

    Parameters:
        db (Session): Una sesión de base de datos.
        user_id (int): El ID del usuario a obtener.

    Returns:
        User: El objeto User correspondiente al usuario con el ID especificado.

    """
    return db.query(user_models.User).filter(
        user_models.User.id == user_id
    ).first()


def get_user_by_name(db: Session, user_name: str) -> User:
    """
    Obtiene un usuario de la base de datos por su nombre de usuario.

    Parameters:
        db (Session): Una sesión de base de datos.
        user_name (str): El nombre de usuario del usuario a obtener.

    Returns:
        User: El objeto User correspondiente al usuario con el nombre de usuario especificado.

    """
    return db.query(user_models.User).filter(
        user_models.User.user == user_name
    ).first()


def update_user(db: Session, user_old: User, password: str):
    """
    Actualiza la contraseña de un usuario en la base de datos.

    Copy code
    Parameters:
        db (Session): Una sesión de base de datos.
        user_old (User): El objeto User que se actualizará.
        password (str): La nueva contraseña para el usuario.

    Returns:
        User: El objeto User actualizado.

    """
    hashed_password = pwd_context.hash(password)
    user_old.password = hashed_password
    db.commit()
    return user_old


def delete_user(db: Session, user_db: user_models.User):
    """
    Elimina un usuario de la base de datos.

    Parameters:
        db (Session): Una sesión de base de datos.
        user_db (User): El objeto User que se eliminará.

    """
    db.delete(user_db)
    db.commit()
