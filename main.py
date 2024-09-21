from fastapi import FastAPI

from repository import contacts
from routes import contacts, auth
# from contacts_api_2 import models, schemas
# from db import engine

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}


#  uvicorn main:app --reload