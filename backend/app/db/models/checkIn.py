from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.session import Base

class CheckIn(Base):
    __tablename__ = "check_ins"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)

    # Relationships
    employee = relationship("User")
    check_out = relationship("CheckOut", back_populates="check_in", uselist=False)  # One-to-one relationship

    def __init__(self, employee_id, date, time):
        self.employee_id = employee_id
        self.date = date
        self.time = time
