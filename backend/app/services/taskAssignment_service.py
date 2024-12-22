from sqlalchemy.orm import Session
from app.db.models.taskAssignment import TaskAssignment
from app.schemas.taskAssignment import TaskAssignmentCreate
from functools import wraps
from app.services.auth_service import get_current_user
from fastapi import Depends
from app.db.models.users import User

def role_required(allowed_roles):
    """
    Decorator to enforce role-based restrictions.
    :param allowed_roles: List of roles allowed to access the function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, current_user: User = Depends(get_current_user), **kwargs):
            # Check user role
            if not current_user or current_user.role not in allowed_roles:
                raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@role_required(["HR"])
def assign_task(db: Session, assignment: TaskAssignmentCreate):
    db_assignment = TaskAssignment(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

@role_required(["Employee", "HR"])
def get_task_assignments(db: Session, task_id: int):
    return db.query(TaskAssignment).filter(TaskAssignment.task_id == task_id).all()

@role_required(["Employee", "HR"])
def get_user_assignments(db: Session, user_id: int):
    return db.query(TaskAssignment).filter(TaskAssignment.user_id == user_id).all()

@role_required(["HR"])
def remove_assignment(db: Session, assignment_id: int):
    db_assignment = db.query(TaskAssignment).filter(TaskAssignment.id == assignment_id).first()
    db.delete(db_assignment)
    db.commit()


