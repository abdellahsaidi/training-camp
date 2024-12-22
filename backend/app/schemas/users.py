from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserBase(BaseModel):
    first_name: str
    second_name: str
    email: EmailStr
    role: Optional[str] = "Employee"
    position: Optional[str] = None
    profile_picture: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str]
    second_name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    position: Optional[str]
    profile_picture: Optional[str]

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True
