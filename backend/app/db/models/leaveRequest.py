from sqlalchemy import Column, Integer, Text, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from app.session import Base

class LeaveRequest(Base):
    __tablename__ = "leave_requests"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    reason = Column(Text, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String, default="Pending")  # Status: Pending, Approved, Rejected
    
    # Relationships
    employee = relationship("User", back_populates="leave_requests")

    def __init__(self, employee_id, reason, start_date, end_date, status="Pending"):
        self.employee_id = employee_id
        self.reason = reason
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
