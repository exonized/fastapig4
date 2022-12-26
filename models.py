import sqlalchemy
import database

usersbdd = sqlalchemy.Table(
    "users",
    database.metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER , primary_key=True),
    sqlalchemy.Column("users", sqlalchemy.String),
    sqlalchemy.Column("mdp", sqlalchemy.String),
)