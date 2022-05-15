from pydantic import BaseModel, validator
import re


class Employee(BaseModel):
    id: int
    first_name: str
    surname: str
    created_at: str = None

    @validator("id")
    def validate_id(cls, p):
        if not p:
            raise ValueError("id is required")
        elif p < 0:
            raise ValueError("id must be positive")
        elif not isinstance(p, int):
            raise ValueError("id must be an integer")
        return p

    @validator("first_name")
    def validate_first_name(cls, p):
        p = p.lower()
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
        return p

    @validator("surname")
    def validate_surname(cls, p):
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