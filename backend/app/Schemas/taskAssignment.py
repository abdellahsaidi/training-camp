from pydantic import BaseModel, EmailStr
from typing import Optional, List

class TaskAssignmentBase(BaseModel):
    task_id: int
    user_id: int

class TaskAssignmentCreate(TaskAssignmentBase):
    pass

class TaskAssignmentResponse(TaskAssignmentBase):
    id: int
    class Config:
        orm_mode = True
