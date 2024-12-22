from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.session import Base

class TaskAssignment(Base):
    __tablename__ = "task_assignments"
    
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    task = relationship("Task", back_populates="assigned_users")
    user = relationship("User", back_populates="tasks")

    def __init__(self, task_id, user_id):
        self.task_id = task_id
        self.user_id = user_id
