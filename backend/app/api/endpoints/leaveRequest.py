from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.leaveRequest import LeaveRequestCreate, LeaveRequestUpdate, LeaveRequestResponse
from app.services.leaveRequest_service import get_leave_request, get_employee_leave_requests, create_leave_request, update_leave_request, delete_leave_request
from app.session import get_db
from app.services.auth_service import get_current_user
from app.db.models.users import User

router = APIRouter()

@router.get("/", response_model=list[LeaveRequestResponse])
def list_leave_requests(employee_id: int = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    if employee_id:
        return get_employee_leave_requests(db, employee_id, skip=skip, limit=limit)
    return []  # Return global leave requests if needed

@router.get("/{leave_id}", response_model=LeaveRequestResponse)
def read_leave_request(leave_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    db_leave = get_leave_request(db, leave_id)
    if not db_leave:
        raise HTTPException(status_code=404, detail="Leave request not found")
    return db_leave

@router.post("/", response_model=LeaveRequestResponse)
def create_new_leave_request(leave_request: LeaveRequestCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_leave_request(db, leave_request, employee_id=1)  # Replace with the authenticated user's ID

@router.put("/{leave_id}", response_model=LeaveRequestResponse)
def update_existing_leave_request(leave_id: int, leave_update: LeaveRequestUpdate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return update_leave_request(db, leave_id, leave_update)

@router.delete("/{leave_id}")
def delete_existing_leave_request(leave_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    delete_leave_request(db, leave_id)
    return {"detail": "Leave request deleted successfully"}