import sqlalchemy.orm as _orm

import passlib.hash as _hash

import fastapi
import fastapi.security as _security

import models
import schemas
import database


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_items(db:  _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(item: schemas.ItemCreate, db:  _orm.Session):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def contact_create(contact: schemas.ContactCreate, db: _orm.Session):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contact(db:  _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Contact).offset(skip).limit(limit).all()


def get_services(db:  _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(models.Services).offset(skip).limit(limit).all()


def create_services(services: schemas.ServiceCreate, db:  _orm.Session):
    db_services = models.Services(**services.dict())
    db.add(db_services)
    db.commit()
    db.refresh(db_services)
    return db_services
