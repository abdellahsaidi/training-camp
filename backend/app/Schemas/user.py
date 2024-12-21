from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for creating a user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "Employee"  # Default role
    position: Optional[str] = None
    profile_picture: Optional[str] = None

# Schema for updating a user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None
    position: Optional[str] = None
    profile_picture: Optional[str] = None
