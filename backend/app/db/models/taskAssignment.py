from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class TaskAssignment(Base):
    __tablename__ = "task_assignments"
    
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    task = relationship("Task", back_populates="assigned_users")
    user = relationship("User", back_populates="tasks")
