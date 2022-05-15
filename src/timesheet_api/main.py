from statistics import mode
from fastapi import FastAPI
from routers.timesheet import router as timesheet_router
from database import engine
import models
import os

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

prefix = os.getenv("API_PREFIX", "")

app.include_router(router=timesheet_router, prefix="{prefix}timesheet".format(prefix=prefix))
