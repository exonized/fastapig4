import sqlalchemy
from database import metadata



class User(sqlalchemy.Table):
    "users",
    metadata,
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    pseudo = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    roles = sqlalchemy.Column(sqlalchemy.String,  default=('Membre'))
    avatar = sqlalchemy.Column(sqlalchemy.String, default=('Avatar/base.png'))
    hashed_password = sqlalchemy.Column(sqlalchemy.String)

