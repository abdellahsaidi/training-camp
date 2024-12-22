from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class AbsenceBase(BaseModel):
    date: date
    status: str
    justification: Optional[str] = None

class AbsenceCreate(AbsenceBase):
    pass

class AbsenceResponse(AbsenceBase):
    id: int
    employee_id: int
    class Config:
        orm_mode = True
