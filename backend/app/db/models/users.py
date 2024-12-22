from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.session import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    firtName = Column(String, nullable=False)
    secondName = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="Employee")  # Roles: Employee, HR, Admin
    position = Column(String, nullable=True)  # Job title (e.g., "Marketing Manager")
    profile_picture = Column(String, default=None)

    # Relationships
    tasks = relationship("TaskAssignment", back_populates="user")
    checkIn_records = relationship("CheckIn", back_populates="employee")
    checkOut_records = relationship("CheckOut", back_populates="employee")
    absences = relationship("Absence", back_populates="employee")
    created_tasks = relationship("Task", back_populates="created_by_user")