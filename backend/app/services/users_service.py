from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.db.models.users import User
from app.schemas.users import UserCreate, UserUpdate
from functools import wraps
from app.services.auth_service import get_current_user
from passlib.context import CryptContext


def role_required(allowed_roles):
    """
    Decorator to enforce role-based restrictions.
    :param allowed_roles: List of roles allowed to access the function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, current_user: User = Depends(get_current_user), **kwargs):
            # Check user role
            if not current_user or current_user.role not in allowed_roles:
                raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@role_required(["Admin", "HR"])
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

@role_required(["Admin", "HR"])
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a plain-text password."""
    return pwd_context.hash(password)


@role_required(["Admin"])
def create_user(user: UserCreate, db: Session ):
    # Hash the incoming password
    hashed_password = hash_password(user.password)
    new_user = {
        "id": user.id,
        "first_name": user.firstName,
        "second_name": user.secondName,
        "email": user.email,
        "role": user.role,
        "position": user.position,
        "password": hashed_password 
    }
    db_user = User.model_validate(new_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@role_required(["Admin", "Employee"])
def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@role_required(["Admin"])
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
