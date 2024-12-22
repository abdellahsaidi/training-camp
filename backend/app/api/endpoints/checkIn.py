from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.checkIn import CheckInCreate, CheckInResponse
from app.services.checkIn_service import create_check_in, get_employee_check_ins
from app.session import get_db
from app.services.auth_service import get_current_user
from app.db.models.users import User

router = APIRouter()

@router.post("/check-in", response_model=CheckInResponse)
def create_employee_check_in(check_in: CheckInCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_check_in(db, check_in, employee_id=1)  


@router.get("/user/{user_id}/check-ins", response_model=list[CheckInResponse])
def list_employee_check_ins(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return get_employee_check_ins(db, user_id, skip=skip, limit=limit)

