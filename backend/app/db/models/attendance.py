from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.session import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    check_in_time = Column(DateTime, nullable=True)
    check_out_time = Column(DateTime, nullable=True)

    # Relationship to User model
    user = relationship("User", back_populates="attendances")

    def __init__(self, user_id: int, check_in_time: datetime = None, check_out_time: datetime = None):
        self.user_id = user_id
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
