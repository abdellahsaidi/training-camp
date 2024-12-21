from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.taskAssignment import TaskAssignmentCreate
from app.services.taskAssignment_service import assign_task, get_task_assignments, get_user_assignments, remove_assignment
from app.session import get_db

router = APIRouter()

@router.post("/assign", response_model=dict)
def assign_new_task(task_assignment: TaskAssignmentCreate, db: Session = Depends(get_db)):
    assign_task(db, task_assignment)
    return {"detail": "Task assigned successfully"}

@router.get("/task/{task_id}/assignments", response_model=list[dict])
def list_task_assignments(task_id: int, db: Session = Depends(get_db)):
    return get_task_assignments(db, task_id)

@router.get("/user/{user_id}/assignments", response_model=list[dict])
def list_user_assignments(user_id: int, db: Session = Depends(get_db)):
    return get_user_assignments(db, user_id)

@router.delete("/assignment/{assignment_id}", response_model=dict)
def remove_task_assignment(assignment_id: int, db: Session = Depends(get_db)):
    remove_assignment(db, assignment_id)
    return {"detail": "Task assignment removed successfully"}