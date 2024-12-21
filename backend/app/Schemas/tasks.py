from pydantic import BaseModel, EmailStr
from typing import Optional, List

class TaskBase(BaseModel):
    title: str
    description: str
    status: Optional[str] = "Pending"

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]

class TaskResponse(TaskBase):
    id: int
    created_by: int
    class Config:
        orm_mode = True
