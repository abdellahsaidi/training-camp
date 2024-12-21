from sqlalchemy.orm import Session
from app.db.models.absence import Absence
from app.schemas.absence import AbsenceCreate

def get_absence(db: Session, absence_id: int):
    return db.query(Absence).filter(Absence.id == absence_id).first()

def get_employee_absences(db: Session, employee_id: int, skip: int = 0, limit: int = 10):
    return db.query(Absence).filter(Absence.employee_id == employee_id).offset(skip).limit(limit).all()

def create_absence(db: Session, absence: AbsenceCreate, employee_id: int):
    db_absence = Absence(**absence.dict(), employee_id=employee_id)
    db.add(db_absence)
    db.commit()
    db.refresh(db_absence)
    return db_absence

def delete_absence(db: Session, absence_id: int):
    db_absence = db.query(Absence).filter(Absence.id == absence_id).first()
    db.delete(db_absence)
    db.commit()
