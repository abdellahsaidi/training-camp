from datetime import time , date
from pydantic import BaseModel, EmailStr
from typing import Optional, List
class CheckInBase(BaseModel):
    date: date
    time: time

class CheckInCreate(CheckInBase):
    pass

class CheckInResponse(CheckInBase):
    id: int
    employee_id: int
    class Config:
        orm_mode = True