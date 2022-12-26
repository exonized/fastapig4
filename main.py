import databases


import fastapi.security as _security
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

import pydantic as _pydantic
import sqlalchemy.orm as _orm

from database import metadata, engine


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]



metadata.create_all(engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class _UserBase(_pydantic.BaseModel):
    email: str
    pseudo :str
    avatar: str
    roles : str

class UserCreate(_UserBase):
    hashed_password: str
    

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True



def get_db():
    db =  databases.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}

