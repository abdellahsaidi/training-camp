from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AttendanceBase(BaseModel):
    user_id: int
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None

    class Config:
        orm_mode = True


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase):
    id: int
    user_id: int
    check_in_time: Optional[datetime]
    check_out_time: Optional[datetime]
