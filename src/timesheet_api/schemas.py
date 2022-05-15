from lib2to3.pytree import Base
from pydantic import BaseModel, validator
import re


class Timesheet(BaseModel):
    id: int
    employee_id: int = None
    employee_name: str = None
    date: str = None
    hours: int
    description: str

    @validator("id")
    def validate_id(cls, p):
        if not p:
            raise ValueError("id is required")
        elif p < 0:
            raise ValueError("id must be positive")
        elif not isinstance(p, int):
            raise ValueError("id must be an integer")
        return p

    @validator("date")
    def validate_date(cls, p):
        if not p:
            raise ValueError("date is required")
        elif not isinstance(p, str):
            raise ValueError("date must be a string")
        elif len(p) < 3:
            raise ValueError("date must be at least 3 characters long")
        return p

    @validator("hours")
    def validate_hours(cls, p):
        if not p:
            raise ValueError("hours is required")
        elif p < 0:
            raise ValueError("hours must be positive")
        elif not isinstance(p, int):
            raise ValueError("hours must be an integer")
        elif p > 12:
            raise ValueError("hours must be less than 12")
        return p

    @validator("description")
    def validate_description(cls, p):
        p = p.lower()
        original_p = p
        p.replace(" ", "")
        # check if the name are not numbers with re
        if re.findall(r"\d", p):
            raise ValueError("name must not contain numbers/special characters")
        if not p:
            raise ValueError("name is required")
        elif not isinstance(p, str):
            raise ValueError("name must be a string")
        elif len(p) < 3:
            raise ValueError("name must be at least 3 characters long")
        return original_p