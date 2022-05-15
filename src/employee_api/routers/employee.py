from fastapi import APIRouter, Depends, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session
from models import Employee as EmployeeModel
from schemas import Employee as EmployeeSchema
from datetime import datetime

router = APIRouter()

def get_db() -> Session:
    """
    Complete the full cycle of a db session (open, close).
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get('/', tags=["employee"])
async def get_a_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(EmployeeModel).filter(EmployeeModel.id == emp_id).first()
    if employee:
        return employee
    else:
        raise HTTPException(status_code=404, detail=('Employee not found'))

@router.get('/all/', tags=["employee"])
async def get_employees(db: Session = Depends(get_db)):
    return db.query(EmployeeModel).all()

@router.post('/add/', tags=["employee"], status_code=201)
async def add_employee(employee: EmployeeSchema, db: Session = Depends(get_db)):
    try:
        if db.query(EmployeeModel).filter(EmployeeModel.id == employee.id).first():
            raise HTTPException(status_code=400, detail="Employee already exists")
        new_employee = EmployeeModel(id=employee.id, 
                                    first_name=employee.first_name,
                                    surname=employee.surname,
                                    created_at=datetime.now())
        db.add(new_employee)
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    else:
        db.commit()
        return {"employee": db.query(EmployeeModel).filter(EmployeeModel.id == employee.id).first()}
