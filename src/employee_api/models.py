from database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)