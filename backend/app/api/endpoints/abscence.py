from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.session import get_db
from app.schemas.abscence import AbsenceCreate , AbsenceResponse
from app.db.models.abscence import Absence
from app.services.abscence_service import (
    get_absence,
    get_employee_absences,
    create_absence,
    delete_absence,
)
from app.services.auth_service import get_current_user
from app.db.models.users import User
from typing import List

router = APIRouter()

# Get absence by ID
@router.get("/{absence_id}", response_model=AbsenceResponse)
def read_absence(absence_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    absence = get_absence(db, absence_id)
    if not absence:
        raise HTTPException(status_code=404, detail="Absence not found")
    return absence

# Get all absences for a specific employee
@router.get("/employee/{employee_id}", response_model=List[AbsenceResponse])
def read_employee_absences(
    employee_id: int,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    absences = get_employee_absences(db, employee_id, skip, limit)
    return absences

# Create a new absence
@router.post("/", response_model=AbsenceResponse, status_code=status.HTTP_201_CREATED)
def create_new_absence(
    absence: AbsenceCreate,
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Only authorized roles should access this route
    if current_user.role not in ["HR"]:
        raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
    return create_absence(db, absence, employee_id)

# Delete an absence by ID
@router.delete("/{absence_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_absence(absence_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Only authorized roles should access this route
    if current_user.role not in ["HR"]:
        raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
    absence = get_absence(db, absence_id)
    if not absence:
        raise HTTPException(status_code=404, detail="Absence not found")
    delete_absence(db, absence_id)
    return {"message": "Absence deleted successfully"}
