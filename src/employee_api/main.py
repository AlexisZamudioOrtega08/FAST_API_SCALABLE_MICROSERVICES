from statistics import mode
from fastapi import FastAPI
from routers.employee import router as employee_router
from database import engine
import models
import os

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

prefix = os.getenv("API_PREFIX", "")

app.include_router(router=employee_router, prefix="{prefix}employee".format(prefix=prefix))
