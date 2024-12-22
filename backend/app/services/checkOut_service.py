from sqlalchemy.orm import Session
from app.db.models.checkOut import CheckOut
from app.schemas.checkOut import CheckOutCreate
from app.services.auth_service import get_current_user
from fastapi import Depends
from app.db.models.users import User
from functools import wraps

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


@role_required(["Admin"])
def get_check_out(db: Session, check_out_id: int):
    return db.query(CheckOut).filter(CheckOut.id == check_out_id).first()

@role_required(["Admin"])
def get_employee_check_outs(db: Session, employee_id: int, skip: int = 0, limit: int = 10):
    return db.query(CheckOut).filter(CheckOut.employee_id == employee_id).offset(skip).limit(limit).all()

@role_required(["Admin"])
def create_check_out(db: Session, check_out: CheckOutCreate, employee_id: int):
    db_check_out = CheckOut(**check_out.dict(), employee_id=employee_id)
    db.add(db_check_out)
    db.commit()
    db.refresh(db_check_out)
    return db_check_out
