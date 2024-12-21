from sqlalchemy.orm import Session
from app.db.models.checkOut import CheckOut
from app.schemas.checkOut import CheckOutCreate



# Check-Out CRUD
def get_check_out(db: Session, check_out_id: int):
    return db.query(CheckOut).filter(CheckOut.id == check_out_id).first()

def get_employee_check_outs(db: Session, employee_id: int, skip: int = 0, limit: int = 10):
    return db.query(CheckOut).filter(CheckOut.employee_id == employee_id).offset(skip).limit(limit).all()

def create_check_out(db: Session, check_out: CheckOutCreate, employee_id: int):
    db_check_out = CheckOut(**check_out.dict(), employee_id=employee_id)
    db.add(db_check_out)
    db.commit()
    db.refresh(db_check_out)
    return db_check_out
