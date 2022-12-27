import sqlalchemy
from database import metadata

usersbdd = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER , primary_key=True),
    sqlalchemy.Column("users", sqlalchemy.String),
    sqlalchemy.Column("mdp", sqlalchemy.String),
)



class User(sqlalchemy.Table):
    "users",
    metadata,
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    pseudo = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    roles = sqlalchemy.Column(sqlalchemy.String,  default=('Membre'))
    avatar = sqlalchemy.Column(sqlalchemy.String, default=('Avatar/base.png'))
    hashed_password = sqlalchemy.Column(sqlalchemy.String)

    
    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)