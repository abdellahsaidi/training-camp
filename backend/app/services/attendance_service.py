from sqlalchemy.orm import Session
from fastapi import Depends
from datetime import time , date
from app.db.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate
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

@role_required(["HR","Employee"])
def get_attendance(db: Session, attendance_id: int):
    return db.query(Attendance).filter(Attendance.id == attendance_id).first()

@role_required(["HR","Employee"])
def get_user_attendances(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Attendance).filter(Attendance.user_id == user_id).offset(skip).limit(limit).all()


def create_attendance(db: Session, attendance: AttendanceCreate, user_id: int):
    db_attendance = Attendance(**attendance.dict(), user_id=user_id)  
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def update_attendance_check_out(db: Session, attendance_id: int, check_out_time: date):
    attendance = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if attendance:
        attendance.check_out_time = check_out_time
        db.commit()
        db.refresh(attendance)
    return attendance


def delete_attendance(db: Session, attendance_id: int):
    attendance = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if attendance:
        db.delete(attendance)
        db.commit()
    return attendance


@role_required(["HR","Employee"])
def get_attendance_history(
    user_id: int,
    db: Session
):
    attendances = db.query(Attendance).filter(Attendance.user_id == user_id).all()
    return {"attendance_history": attendances}