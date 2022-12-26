import sqlalchemy
from database import metadata

usersbdd = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER , primary_key=True),
    sqlalchemy.Column("users", sqlalchemy.String),
    sqlalchemy.Column("mdp", sqlalchemy.String),
)
