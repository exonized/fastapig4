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
