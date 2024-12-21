from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from models import User, Task, TaskAssignment, LeaveRequest, CheckOut
from schemas.user import UserCreate, UserUpdate
from schemas.task import TaskCreate, TaskUpdate, TaskAssignmentCreate
from schemas.leave_request import LeaveRequestCreate, LeaveRequestUpdate
from schemas.check_out import CheckOutCreate

app = FastAPI(title="DashRH")



# User CRUD
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

# Task CRUD
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}

# Task Assignment CRUD
@app.post("/task-assignments/", response_model=TaskAssignment)
def create_task_assignment(task_assignment: TaskAssignmentCreate, db: Session = Depends(get_db)):
    db_assignment = TaskAssignment(**task_assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

@app.get("/task-assignments/{assignment_id}", response_model=TaskAssignment)
def get_task_assignment(assignment_id: int, db: Session = Depends(get_db)):
    assignment = db.query(TaskAssignment).filter(TaskAssignment.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Task assignment not found")
    return assignment

@app.delete("/task-assignments/{assignment_id}", response_model=dict)
def delete_task_assignment(assignment_id: int, db: Session = Depends(get_db)):
    db_assignment = db.query(TaskAssignment).filter(TaskAssignment.id == assignment_id).first()
    if not db_assignment:
        raise HTTPException(status_code=404, detail="Task assignment not found")
    db.delete(db_assignment)
    db.commit()
    return {"message": "Task assignment deleted successfully"}

# Leave Request CRUD
@app.post("/leave-requests/", response_model=LeaveRequest)
def create_leave_request(leave_request: LeaveRequestCreate, db: Session = Depends(get_db)):
    db_request = LeaveRequest(**leave_request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

@app.get("/leave-requests/{request_id}", response_model=LeaveRequest)
def get_leave_request(request_id: int, db: Session = Depends(get_db)):
    request = db.query(LeaveRequest).filter(LeaveRequest.id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Leave request not found")
    return request

@app.put("/leave-requests/{request_id}", response_model=LeaveRequest)
def update_leave_request(request_id: int, leave_request: LeaveRequestUpdate, db: Session = Depends(get_db)):
    db_request = db.query(LeaveRequest).filter(LeaveRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(status_code=404, detail="Leave request not found")
    for key, value in leave_request.dict(exclude_unset=True).items():
        setattr(db_request, key, value)
    db.commit()
    db.refresh(db_request)
    return db_request

@app.delete("/leave-requests/{request_id}", response_model=dict)
def delete_leave_request(request_id: int, db: Session = Depends(get_db)):
    db_request = db.query(LeaveRequest).filter(LeaveRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(status_code=404, detail="Leave request not found")
    db.delete(db_request)
    db.commit()
    return {"message": "Leave request deleted successfully"}

# CheckOut CRUD
@app.post("/check-outs/", response_model=CheckOut)
def create_check_out(check_out: CheckOutCreate, db: Session = Depends(get_db)):
    db_check_out = CheckOut(**check_out.dict())
    db.add(db_check_out)
    db.commit()
    db.refresh(db_check_out)
    return db_check_out

@app.get("/check-outs/{check_out_id}", response_model=CheckOut)
def get_check_out(check_out_id: int, db: Session = Depends(get_db)):
    check_out = db.query(CheckOut).filter(CheckOut.id == check_out_id).first()
    if not check_out:
        raise HTTPException(status_code=404, detail="Check-out record not found")
    return check_out

@app.delete("/check-outs/{check_out_id}", response_model=dict)
def delete_check_out(check_out_id: int, db: Session = Depends(get_db)):
    db_check_out = db.query(CheckOut).filter(CheckOut.id == check_out_id).first()
    if not db_check_out:
        raise HTTPException(status_code=404, detail="Check-out record not found")
    db.delete(db_check_out)
    db.commit()
    return {"message": "Check-out record deleted successfully"}

# Create CheckIn
def create_check_in(db: Session, check_in_data: CheckInCreate):
    db_check_in = CheckIn(**check_in_data.dict())
    db.add(db_check_in)
    db.commit()
    db.refresh(db_check_in)
    return db_check_in

# Get CheckIn by ID
def get_check_in(db: Session, check_in_id: int):
    return db.query(CheckIn).filter(CheckIn.id == check_in_id).first()

# Get All CheckIns
def get_check_ins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CheckIn).offset(skip).limit(limit).all()

# Update CheckIn
def update_check_in(db: Session, check_in_id: int, check_in_data: CheckInUpdate):
    db_check_in = get_check_in(db, check_in_id)
    if not db_check_in:
        return None
    for key, value in check_in_data.dict(exclude_unset=True).items():
        setattr(db_check_in, key, value)
    db.commit()
    db.refresh(db_check_in)
    return db_check_in

# Delete CheckIn
def delete_check_in(db: Session, check_in_id: int):
    db_check_in = get_check_in(db, check_in_id)
    if db_check_in:
        db.delete(db_check_in)
        db.commit()
    return db_check_in

# Create Absence
def create_absence(db: Session, absence_data: AbsenceCreate):
    db_absence = Absence(**absence_data.dict())
    db.add(db_absence)
    db.commit()
    db.refresh(db_absence)
    return db_absence

# Get Absence by ID
def get_absence(db: Session, absence_id: int):
    return db.query(Absence).filter(Absence.id == absence_id).first()

# Get All Absences
def get_absences(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Absence).offset(skip).limit(limit).all()

# Update Absence
def update_absence(db: Session, absence_id: int, absence_data: AbsenceUpdate):
    db_absence = get_absence(db, absence_id)
    if not db_absence:
        return None
    for key, value in absence_data.dict(exclude_unset=True).items():
        setattr(db_absence, key, value)
    db.commit()
    db.refresh(db_absence)
    return db_absence

# Delete Absence
def delete_absence(db: Session, absence_id: int):
    db_absence = get_absence(db, absence_id)
    if db_absence:
        db.delete(db_absence)
        db.commit()
    return db_absence
