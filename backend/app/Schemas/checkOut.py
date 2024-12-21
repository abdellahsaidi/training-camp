from datetime import time , date
from pydantic import BaseModel, EmailStr
from typing import Optional, List
class CheckOutBase(BaseModel):
    date: date
    time: time
    check_in_id: int

class CheckOutCreate(CheckOutBase):
    pass

class CheckOutResponse(CheckOutBase):
    id: int
    employee_id: int
    class Config:
        orm_mode = True