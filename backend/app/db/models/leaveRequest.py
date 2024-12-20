from sqlalchemy import Column, Integer, Text, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class LeaveRequest(Base):
    __tablename__ = "leave_requests"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    reason = Column(Text, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String, default="Pending")  # Status: Pending, Approved, Rejected
    processed_by = Column(Integer, ForeignKey("users.id"))

    # Relationships
    employee = relationship("User", back_populates="leave_requests")
