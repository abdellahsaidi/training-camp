from sqlalchemy.orm import Session
from app.db.models.taskAssignment import TaskAssignment
from app.schemas.taskAssignment import TaskAssignmentCreate

def assign_task(db: Session, assignment: TaskAssignmentCreate):
    db_assignment = TaskAssignment(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

def get_task_assignments(db: Session, task_id: int):
    return db.query(TaskAssignment).filter(TaskAssignment.task_id == task_id).all()

def get_user_assignments(db: Session, user_id: int):
    return db.query(TaskAssignment).filter(TaskAssignment.user_id == user_id).all()

def remove_assignment(db: Session, assignment_id: int):
    db_assignment = db.query(TaskAssignment).filter(TaskAssignment.id == assignment_id).first()
    db.delete(db_assignment)
    db.commit()
