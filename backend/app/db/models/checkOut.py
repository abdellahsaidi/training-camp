from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.session import Base

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

    def __init__(self, employee_id, check_in_id, date, time):
        self.employee_id = employee_id
        self.check_in_id = check_in_id
        self.date = date
        self.time = time
