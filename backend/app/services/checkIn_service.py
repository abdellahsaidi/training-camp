from sqlalchemy.orm import Session
from app.db.models.checkIn import CheckIn
from app.schemas.checkIn import CheckInCreate


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

