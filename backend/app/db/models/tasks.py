from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.session import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String, default="Pending")  # Status: Pending, Completed
    created_by = Column(Integer, ForeignKey("users.id"))

    # Relationships
    assigned_users = relationship("TaskAssignment", back_populates="task")
    created_by_user = relationship("User", back_populates="created_tasks", foreign_keys=[created_by])


    
