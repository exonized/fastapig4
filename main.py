from typing import List

import fastapi
import fastapi.security as _security

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import crud
import models
import schemas
from database import SessionLocal, engine

import sqlalchemy.orm as _orm

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API items (articles)


@app.post("/api/items/", tags=["items"], response_model=schemas.Item)
def create_item_for_user(
    item: schemas.ItemCreate, db: _orm.Session = fastapi.Depends(crud.get_db)
):
    return crud.create_user_item(db=db, item=item)


@app.get("/api/items/get", tags=["items"], response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: _orm.Session = fastapi.Depends(crud.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


# API contact


@app.post("/api/contact/", tags=["contact"], response_model=schemas.Contact)
def create_contact_for_user(
    contact: schemas.ContactCreate, db: _orm.Session = fastapi.Depends(crud.get_db)
):
    return crud.contact_create(db=db, contact=contact)


@app.get("/api/contact/get", tags=["contact"], response_model=List[schemas.Contact])
def read_contact(skip: int = 0, limit: int = 10, db: _orm.Session = fastapi.Depends(crud.get_db)):
    contact = crud.get_contact(db, skip=skip, limit=limit)
    return contact


# API services (services)


@app.post("/api/services/", tags=["services"], response_model=schemas.Service)
def create_services(
    services: schemas.ServiceCreate, db: _orm.Session = fastapi.Depends(crud.get_db)
):
    return crud.create_services(db=db, services=services)


@app.get("/api/services/get", tags=["services"], response_model=List[schemas.Service])
def read_services(skip: int = 0, limit: int = 10, db: _orm.Session = fastapi.Depends(crud.get_db)):
    services = crud.get_services(db, skip=skip, limit=limit)
    return services


@app.get("/", tags=["api"])
def read_services():
    return "API ANTHONY"
