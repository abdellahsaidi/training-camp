from sqlalchemy.orm import Session
from app.db.models.leaveRequest import LeaveRequest
from app.schemas.leaveRequest import LeaveRequestCreate, LeaveRequestUpdate
from functools import wraps
from app.services.auth_service import get_current_user
from fastapi import Depends
from app.db.models.users import User

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
def get_leave_request(db: Session, leave_id: int):
    return db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

@role_required(["HR"])
def get_employee_leave_requests(db: Session, employee_id: int, skip: int = 0, limit: int = 10):
    return db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id).offset(skip).limit(limit).all()

@role_required(["HR"])
def create_leave_request(db: Session, leave_request: LeaveRequestCreate, employee_id: int):
    db_leave = LeaveRequest(**leave_request.dict(), employee_id=employee_id)
    db.add(db_leave)
    db.commit()
    db.refresh(db_leave)
    return db_leave

@role_required(["HR"])
def update_leave_request(db: Session, leave_id: int, leave_update: LeaveRequestUpdate):
    db_leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    for key, value in leave_update.dict(exclude_unset=True).items():
        setattr(db_leave, key, value)
    db.commit()
    db.refresh(db_leave)
    return db_leave

@role_required(["HR"])
def delete_leave_request(db: Session, leave_id: int):
    db_leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    db.delete(db_leave)
    db.commit()
