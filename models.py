import sqlalchemy
import database as _database
from database import metadata

Utilisateurs = sqlalchemy.Table(
    "users",
    sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column(sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column(sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column(sqlalchemy.String,  default=('Membre')),
    sqlalchemy.Column(sqlalchemy.String, default=('Avatar/base.png'))
)


