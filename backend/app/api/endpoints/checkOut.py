from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.checkOut import CheckOutCreate, CheckOutResponse
from app.services.checkOut_service import  create_check_out,  get_employee_check_outs
from app.session import get_db
from app.services.auth_service import get_current_user
from app.db.models.users import User

router = APIRouter()



@router.post("/check-out", response_model=CheckOutResponse)
def create_employee_check_out(check_out: CheckOutCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_check_out(db, check_out, employee_id=1)  # Replace with the authenticated user's ID


@router.get("/user/{user_id}/check-outs", response_model=list[CheckOutResponse])
def list_employee_check_outs(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return get_employee_check_outs(db, user_id, skip=skip, limit=limit)