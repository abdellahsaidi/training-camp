from fastapi import  Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models.checkIn import CheckIn
from datetime import time , date
from app.db.models.attendance import Attendance
from app.Schemas.checkIn import CheckInCreate


# Check-In CRUD
def get_check_in(db: Session, check_in_id: int):
    return db.query(CheckIn).filter(CheckIn.id == check_in_id).first()

def get_employee_check_ins(db: Session, employee_id: int, skip: int = 0, limit: int = 10):
    return db.query(CheckIn).filter(CheckIn.employee_id == employee_id).offset(skip).limit(limit).all()

def create_check_in(db: Session, check_in: CheckInCreate, employee_id: int):
    db_check_in = CheckIn(**check_in.dict(), employee_id=employee_id)
    db.add(db_check_in)
    db.commit()
    db.refresh(db_check_in)
    return db_check_in

def check_in(user_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.user_id == user_id, Attendance.check_out_time == None).first()

    if attendance:
        raise HTTPException( status_code=400, detail="User is already checked in."
        )

    new_attendance = Attendance(user_id=user_id,check_in_time=date.utcnow())
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return {"message": "Check-in successful", "attendance": new_attendance}

def facial_check_in(user_id: int, image: bytes, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user :
        raise HTTPException(status_code=404, detail="User not found or no face encoding available")

    known_face_encodings = [user.face_encoding]
    if not validate_face(image, known_face_encodings):
        raise HTTPException(status_code=401, detail="Face recognition failed")

    return check_in(user_id, db)

