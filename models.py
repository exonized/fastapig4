import sqlalchemy
from database import metadata

usersbdd = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER , primary_key=True, index=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("pseudo", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("roles", sqlalchemy.String, default=('Membre')),
    sqlalchemy.Column("avatar", sqlalchemy.String , default=('Avatar/base.png'))
    
)


