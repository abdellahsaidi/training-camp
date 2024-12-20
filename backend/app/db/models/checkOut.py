from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CheckOut(Base):
    __tablename__ = "check_outs"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    check_in_id = Column(Integer, ForeignKey("check_ins.id"), unique=True)  # One-to-one relationship
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)

    # Relationships
    employee = relationship("User")
    check_in = relationship("CheckIn", back_populates="check_out", uselist=False)  # One-to-one relationship
