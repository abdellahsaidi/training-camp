from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime , time
from typing import List
from app.session import get_db
from app.schemas.attendance import AttendanceCreate, AttendanceResponse
from app.services.attendance_service import (
    get_attendance,
    get_user_attendances,
    create_attendance,
    update_attendance_check_out,
    delete_attendance,
    get_attendance_history,
)
from app.services.auth_service import get_current_user
from app.db.models.users import User

router = APIRouter()

# Get attendance by ID
@router.get("/{attendance_id}", response_model=AttendanceResponse)
def read_attendance(attendance_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    attendance = get_attendance(db, attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance

# Get all attendances for a specific user
@router.get("/user/{user_id}", response_model=List[AttendanceResponse])
def read_user_attendances(
    user_id: int,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_user_attendances(db, user_id, skip, limit)

# Create a new attendance record
@router.post("/", response_model=AttendanceResponse, status_code=status.HTTP_201_CREATED)
def create_new_attendance(
    attendance: AttendanceCreate,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_attendance(db, attendance, user_id)

# Update attendance check-out time
@router.put("/{attendance_id}/checkout", response_model=AttendanceResponse)
def update_checkout_time(
    attendance_id: int,
    check_out_time: time,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    attendance = update_attendance_check_out(db, attendance_id, check_out_time)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance

# Delete an attendance record
@router.delete("/{attendance_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_attendance(
    attendance_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    attendance = get_attendance(db, attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    delete_attendance(db, attendance_id)
    return {"message": "Attendance record deleted successfully"}

# Get attendance history for a user
@router.get("/history/{user_id}", response_model=dict)
def read_attendance_history(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_attendance_history(user_id, db)
