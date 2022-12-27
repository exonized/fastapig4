import sqlalchemy

from database import metadata


usersbdd = sqlalchemy.Table(
    "users",
    metadata,
    id = sqlalchemy.Column("id", sqlalchemy.INTEGER , primary_key=True, index=True),
    email = sqlalchemy.Column("email", sqlalchemy.String, unique=True, index=True),
    pseudo = sqlalchemy.Column("pseudo", sqlalchemy.String, unique=True, index=True),
    roles = sqlalchemy.Column("roles", sqlalchemy.String, default=('Membre')),
    avatar = sqlalchemy.Column("avatar", sqlalchemy.String , default=('Avatar/base.png')),
    hashed_password = sqlalchemy.Column("hashed_password", sqlalchemy.String)
)
