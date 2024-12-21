from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.session import Base

class Absence(Base):
    __tablename__ = "absences"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)  # Status: Justified, Not Justified
    justification = Column(Text, nullable=True)

    # Relationships
    employee = relationship("User", back_populates="absences")
