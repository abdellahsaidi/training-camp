from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional, List
class LeaveRequestBase(BaseModel):
    reason: str
    start_date: date
    end_date: date
    status: Optional[str] = "Pending"

class LeaveRequestCreate(LeaveRequestBase):
    pass

class LeaveRequestUpdate(BaseModel):
    reason: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    status: Optional[str]

class LeaveRequestResponse(LeaveRequestBase):
    id: int
    employee_id: int
    processed_by: Optional[int]
    class Config:
        orm_mode = True
