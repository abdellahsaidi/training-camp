from sqlalchemy.orm import Session
from app.db.models.leaveRequest import LeaveRequest
from app.schemas.leaveRequest import LeaveRequestCreate, LeaveRequestUpdate

def get_leave_request(db: Session, leave_id: int):
    return db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

def get_employee_leave_requests(db: Session, employee_id: int, skip: int = 0, limit: int = 10):
    return db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id).offset(skip).limit(limit).all()

def create_leave_request(db: Session, leave_request: LeaveRequestCreate, employee_id: int):
    db_leave = LeaveRequest(**leave_request.dict(), employee_id=employee_id)
    db.add(db_leave)
    db.commit()
    db.refresh(db_leave)
    return db_leave

def update_leave_request(db: Session, leave_id: int, leave_update: LeaveRequestUpdate):
    db_leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    for key, value in leave_update.dict(exclude_unset=True).items():
        setattr(db_leave, key, value)
    db.commit()
    db.refresh(db_leave)
    return db_leave

def delete_leave_request(db: Session, leave_id: int):
    db_leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    db.delete(db_leave)
    db.commit()
