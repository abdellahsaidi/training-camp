from pydantic import BaseModel, EmailStr
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: str
    status: Optional[str] = "Pending"  # Default status
    created_by: int  # Foreign key to `User.id`

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TaskAssignmentCreate(BaseModel):
    task_id: int  # Foreign key to `Task.id`
    user_id: int  # Foreign key to `User.id`