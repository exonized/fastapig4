from typing import List

import fastapi
from fastapi.middleware.cors import CORSMiddleware
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


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Users

@app.post("/api/users", tags=["users"])
async def create_user(
    user: schemas.UserCreate, db: _orm.Session = fastapi.Depends(crud.get_db)
):
    db_user = await crud.get_user_by_email(user.email, db)
    if db_user:
        raise fastapi.HTTPException(
            status_code=400, detail="Votre email est déjà utilisé")

    user = await crud.create_user(user, db)

    return await crud.create_token(user)


@app.post("/api/token", tags=["users"])
async def generate_token(
    form_data: _security.OAuth2PasswordRequestForm = fastapi.Depends(),
    db: _orm.Session = fastapi.Depends(crud.get_db),
):
    user = await crud.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise fastapi.HTTPException(
            status_code=401, detail="Utilisateur non enregistré")

    return await crud.create_token(user)


@app.get("/api/users/me", tags=["users"], response_model=schemas.User)
async def get_user(user: schemas.User = fastapi.Depends(crud.get_current_user)):
    return user


@app.delete("/api/user/me/delete", tags=["users"])
async def delete_user(user: schemas.User = fastapi.Depends(crud.delete_current_user)):
    return user


# API items (articles)


@app.post("/api/items/", tags=["items"], response_model=schemas.Item)
def create_item_for_user(
    item: schemas.ItemCreate, db: _orm.Session = fastapi.Depends(crud.get_db), user: schemas.User = fastapi.Depends(crud.delete_current_user)
):
    return crud.create_user_item(user, db=db, item=item)


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
