from sqlalchemy.orm import Session
from app.db.models.abscence import Absence
from app.schemas.abscence import AbsenceCreate
from app.services.auth_service import get_current_user
from fastapi import Depends
from app.db.models.users import User
from functools import wraps
from typing import List

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

@role_required(["HR","Employee"])
def get_absence(db: Session, absence_id: int):
    return db.query(Absence).filter(Absence.id == absence_id).first()

@role_required(["HR","Employee"])
def get_employee_absences(db: Session, employee_id: int, skip: int = 0, limit: int = 10):
    return db.query(Absence).filter(Absence.employee_id == employee_id).offset(skip).limit(limit).all()

def create_absence(db: Session, absence: AbsenceCreate, employee_id: int):
    db_absence = Absence(**absence.dict(), employee_id=employee_id)
    db.add(db_absence)
    db.commit()
    db.refresh(db_absence)
    return db_absence

def delete_absence(db: Session, absence_id: int):
    db_absence = db.query(Absence).filter(Absence.id == absence_id).first()
    db.delete(db_absence)
    db.commit()
