from sqlalchemy.orm import Session
from app.db.models.tasks import Task 
from app.schemas.tasks import TaskCreate, TaskUpdate
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



@role_required(["Employee", "HR"])
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

@role_required(["Employee", "HR"])
def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

@role_required(["HR"])
def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@role_required(["Employee", "HR"])
def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@role_required(["HR"])
def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(db_task)
    db.commit()


