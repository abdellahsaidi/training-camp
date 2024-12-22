from sqlalchemy.orm import Session
from fastapi import Depends
from datetime import time , date
from app.db.models.attendance import Attendance
from app.Schemas.attendance import AttendanceCreate

def get_attendance(db: Session, attendance_id: int):
    return db.query(Attendance).filter(Attendance.id == attendance_id).first()

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



def get_attendance_history(
    user_id: int,
    db: Session = Depends(get_db)
):
    attendances = db.query(Attendance).filter(Attendance.user_id == user_id).all()
    return {"attendance_history": attendances}
