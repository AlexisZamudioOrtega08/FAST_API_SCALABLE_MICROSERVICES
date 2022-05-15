from os import execvpe
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import Timesheet as TimesheetSchema
from models import Timesheet as TimesheetModel
from datetime import datetime
from database import SessionLocal
import aiohttp


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

@router.get("/all", tags=["timesheet"], status_code=200)
async def get_all_timesheets(db: Session = Depends(get_db)):
    """
    Get all timesheets.
    """
    try:
        timesheets = db.query(TimesheetModel).all()
        return timesheets
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/add/', tags=["timesheet"], status_code=201)
async def add_timesheet_entry(emp_id: str, timesheet: TimesheetSchema, db: Session = Depends(get_db)):
    """
    Add a new timesheet entry.
    """
    if db.query(TimesheetModel).filter(TimesheetModel.id == timesheet.id).first():
        raise HTTPException(status_code=400, detail="Timesheet id already exists")

    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://127.0.0.1:8001/api/v1/employee/?emp_id={}".format(emp_id)
        ) as resp:
            data = await resp.json()
            try:
                data_ = data["id"]
                timesheet = TimesheetModel(
                    id = timesheet.id,
                    employee_id = data["id"],
                    employee_name = data["first_name"] + " " + data["surname"],
                    date = datetime.now(),
                    hours = timesheet.hours,
                    description = timesheet.description
                )
                db.add(timesheet)
            except Exception as e:
                db.rollback()
                raise HTTPException(status_code=400, detail="Employee id does not exist")
            else:
                db.commit()
                return {"timesheet": db.query(TimesheetModel).filter(TimesheetModel.id == timesheet.id).first()}