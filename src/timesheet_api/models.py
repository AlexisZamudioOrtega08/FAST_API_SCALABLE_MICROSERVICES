from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Timesheet(Base):
    __tablename__ = "timesheets"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, nullable=False)
    employee_name = Column(String(50), nullable=False)
    date = Column(DateTime, nullable=False)
    hours = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)