from fastapi import FastAPI

from repository import contacts
from routes import contacts, auth
import models
from db import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')


#  uvicorn main:app --reload