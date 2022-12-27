import sqlalchemy
import sqlalchemy as _sql
import database as _database
from database import metadata

usersbdd = sqlalchemy.Table(
    "users",
    metadata,
    id = sqlalchemy.Column(_sql.Integer, primary_key=True, index=True),
    email = sqlalchemy.Column(_sql.String, unique=True, index=True),
    pseudo = sqlalchemy.Column(_sql.String, unique=True, index=True),
    roles = sqlalchemy.Column(_sql.String,  default=('Membre')),
    avatar = sqlalchemy.Column(_sql.String, default=('Avatar/base.png'))

    
)


