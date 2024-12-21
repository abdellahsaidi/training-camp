from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tasks import TaskCreate, TaskUpdate, TaskResponse
from app.services.tasks_service import get_task, get_tasks, create_task, update_task, delete_task
from app.session import get_db

router = APIRouter()

@router.get("/", response_model=list[TaskResponse])
def list_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db, skip=skip, limit=limit)

@router.get("/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.post("/", response_model=TaskResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.put("/{task_id}", response_model=TaskResponse)
def update_existing_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    return update_task(db, task_id, task_update)

@router.delete("/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    delete_task(db, task_id)
    return {"detail": "Task deleted successfully"}