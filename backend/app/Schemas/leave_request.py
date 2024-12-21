from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class LeaveRequestCreate(BaseModel):
    employee_id: int  # Foreign key to `User.id`
    reason: str
    start_date: date
    end_date: date
    status: Optional[str] = "Pending"  # Default status
    processed_by: Optional[int] = None  # Foreign key to `User.id`

class LeaveRequestUpdate(BaseModel):
    reason: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
    processed_by: Optional[int] = None
