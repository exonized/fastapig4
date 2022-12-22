from typing import List 
import databases
import sqlalchemy

from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "postgresql://cgsukvjjfzlgrd:e980af14f1b9a825d213103d365bb33daeee148528d94274a2f3c8181ca81bec@ec2-52-30-67-143.eu-west-1.compute.amazonaws.com:5432/demsi71c8nc1no"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER , primary_key=True),
    sqlalchemy.Column("users", sqlalchemy.String),
    sqlalchemy.Column("mdp", sqlalchemy.String),
)



engine = sqlalchemy.create_engine(
    DATABASE_URL
)

metadata.create_all(engine)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}